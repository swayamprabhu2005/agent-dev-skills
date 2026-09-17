#!/usr/bin/env python3
"""
audit-gitignore.py - Project Sync Gitignore Auditor

Audits untracked repository files to determine whether .gitignore requires updating.
Suggests precise, minimal rules and prevents dangerous broad wildcards.

Author: SWAYAM KIRAN PRABHU
Part of Project Sync (https://github.com/swayamprabhu/project-sync)
License: MIT
"""

import sys
import subprocess
import json
import argparse
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

COMMON_IGNORE_SUGGESTIONS = [
    (r"(^|[/\\])__pycache__($|[/\\])", "__pycache__/", "Python bytecode cache"),
    (r"\.py[cod]$", "*.py[cod]", "Python compiled files"),
    (r"(^|[/\\])node_modules($|[/\\])", "node_modules/", "Node.js dependencies"),
    (r"(^|[/\\])dist($|[/\\])", "dist/", "Distribution build output"),
    (r"(^|[/\\])build($|[/\\])", "build/", "Compiled build artifacts"),
    (r"(^|[/\\])\.pytest_cache($|[/\\])", ".pytest_cache/", "Pytest cache directory"),
    (r"(^|[/\\])\.venv($|[/\\])", ".venv/", "Python virtual environment"),
    (r"\.DS_Store$", ".DS_Store", "macOS desktop metadata"),
    (r"Thumbs\.db$", "Thumbs.db", "Windows thumbnail cache"),
    (r"\.env(\.local)?$", ".env", "Local environment secrets file"),
    (r"(^|[/\\])\.agent[/\\]scratch($|[/\\])", ".agent/scratch/", "Agent temporary scratch quarantine directory")
]

def run_git(args, cwd=None):
    try:
        res = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
        return res.returncode, res.stdout, res.stderr
    except FileNotFoundError:
        return 127, "", "git executable not found in PATH"

def audit_gitignore(cwd=None):
    code, status_out, _ = run_git(["status", "--porcelain=v1"], cwd=cwd)
    if code != 0:
        return {"error": "Failed to read git status"}

    untracked_files = []
    for line in status_out.splitlines():
        if line.startswith("??"):
            untracked_files.append(line[3:].strip())

    gitignore_path = Path(cwd or ".") / ".gitignore"
    has_gitignore = gitignore_path.exists()
    existing_content = gitignore_path.read_text(encoding="utf-8", errors="replace") if has_gitignore else ""

    recommended_rules = []
    already_covered = []
    unrecognized = []

    for f in untracked_files:
        # Check if git already ignores it (e.g. via global ignore or current rule)
        check_code, check_out, _ = run_git(["check-ignore", "-v", f], cwd=cwd)
        if check_code == 0:
            already_covered.append(f)
            continue

        matched = False
        for pattern, rule, desc in COMMON_IGNORE_SUGGESTIONS:
            if re.search(pattern, f, re.IGNORECASE):
                if rule not in [r["rule"] for r in recommended_rules] and rule not in existing_content:
                    recommended_rules.append({
                        "rule": rule,
                        "description": desc,
                        "triggered_by": f
                    })
                matched = True
                break

        if not matched:
            unrecognized.append(f)

    needs_update = len(recommended_rules) > 0 or not has_gitignore

    return {
        "has_gitignore": has_gitignore,
        "needs_update": needs_update,
        "untracked_count": len(untracked_files),
        "untracked_files": untracked_files,
        "recommended_rules": recommended_rules,
        "already_covered_count": len(already_covered),
        "unrecognized_count": len(unrecognized),
        "unrecognized_files": unrecognized
    }

def main():
    parser = argparse.ArgumentParser(description="Audit .gitignore for Project Sync.")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--path", default=".", help="Path to repository root")
    args = parser.parse_args()

    result = audit_gitignore(cwd=args.path)

    if args.json:
        print(json.dumps(result, indent=2))
        sys.exit(0)

    print("=== Project Sync: .gitignore Audit ===")
    print(f".gitignore exists: {'Yes' if result['has_gitignore'] else 'No (Creation Recommended)'}")
    print(f"Untracked items:   {result['untracked_count']} file(s)")

    if result['recommended_rules']:
        print("\nRecommended .gitignore additions:")
        for rec in result['recommended_rules']:
            print(f"  + {rec['rule']} ({rec['description']}, triggered by '{rec['triggered_by']}')")

    if result['unrecognized_files']:
        print("\nUntracked items not recognized as artifacts (likely project source files):")
        for u in result['unrecognized_files'][:5]:
            print(f"  • {u}")
        if len(result['unrecognized_files']) > 5:
            print(f"  ... and {len(result['unrecognized_files']) - 5} more")

    if not result['needs_update']:
        print("\n[OK] .gitignore is accurate. No additions required.")

if __name__ == "__main__":
    main()
