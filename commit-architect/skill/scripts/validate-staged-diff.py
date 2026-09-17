#!/usr/bin/env python3
"""
validate-staged-diff.py - Commit Architect Staged Diff Validator

Validates staged changes (git diff --cached) before commit creation.
Flags sensitive files, temporary build artifacts, leftover debug prints,
and oversized monolithic diffs.

Author: SWAYAM KIRAN PRABHU
Part of Commit Architect (https://github.com/swayamprabhu/commit-architect)
License: MIT
"""

import sys
import subprocess
import json
import argparse
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

FORBIDDEN_FILES = [
    r"\.env($|\.)",
    r"\.pem$",
    r"\.key$",
    r"credentials\.json$",
    r"id_rsa",
    r"id_ed25519",
    r"\.DS_Store$",
    r"Thumbs\.db$",
    r"\.pyc$",
    r"__pycache__",
    r"node_modules[/\\]",
    r"dist[/\\]",
    r"build[/\\]"
]

SUSPICIOUS_DEBUG_PATTERNS = [
    (r"debugger;", "JavaScript debugger statement"),
    (r"console\.log\(", "Leftover console.log statement"),
    (r"import\s+pdb;\s*pdb\.set_trace\(\)", "Python pdb breakpoint"),
    (r"breakpoint\(\)", "Python built-in breakpoint"),
    (r"binding\.pry", "Ruby binding.pry"),
    (r"fmt\.Println\(", "Go debug println"),
    (r"TODO:\s*remove", "Temporary debug comment")
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

def validate_staged(cwd=None, max_lines=800):
    code, names_out, _ = run_git(["diff", "--cached", "--name-only"], cwd=cwd)
    if code != 0:
        return {"error": "Failed to read git diff"}

    staged_files = [line.strip() for line in names_out.splitlines() if line.strip()]
    if not staged_files:
        return {
            "valid": False,
            "error": "No staged changes found. Use 'git add <file>' to stage changes before committing."
        }

    warnings = []
    errors = []

    # Check forbidden file names
    for f in staged_files:
        for pattern in FORBIDDEN_FILES:
            if re.search(pattern, f, re.IGNORECASE):
                errors.append(f"Forbidden or dangerous file staged: '{f}' (matches pattern {pattern})")

    # Inspect full cached diff
    code, diff_out, _ = run_git(["diff", "--cached"], cwd=cwd)
    diff_lines = diff_out.splitlines()

    additions = sum(1 for line in diff_lines if line.startswith("+") and not line.startswith("+++"))
    deletions = sum(1 for line in diff_lines if line.startswith("-") and not line.startswith("---"))
    total_changed_lines = additions + deletions

    if total_changed_lines > max_lines:
        warnings.append(
            f"Diff size warning: {total_changed_lines} lines changed across {len(staged_files)} files. "
            "Consider whether this change should be divided into smaller logical units."
        )

    # Check for leftover debug statements in added lines
    current_file = None
    for line in diff_lines:
        if line.startswith("+++ b/"):
            current_file = line[6:]
        elif line.startswith("+") and not line.startswith("+++"):
            # Ignore markdown, documentation, or test fixture files for debug prints
            if current_file and not any(current_file.endswith(ext) for ext in [".md", ".txt", ".json", ".csv", ".rst"]):
                for pattern, desc in SUSPICIOUS_DEBUG_PATTERNS:
                    if re.search(pattern, line):
                        warnings.append(f"Suspicious debug code in '{current_file}': {desc} -> {line.strip()[:60]}")

    is_valid = len(errors) == 0

    return {
        "valid": is_valid,
        "staged_file_count": len(staged_files),
        "staged_files": staged_files,
        "additions": additions,
        "deletions": deletions,
        "total_lines": total_changed_lines,
        "errors": errors,
        "warnings": warnings
    }

def main():
    parser = argparse.ArgumentParser(description="Validate staged Git diff for Commit Architect safety.")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--max-lines", type=int, default=800, help="Line threshold to trigger size warning")
    parser.add_argument("--path", default=".", help="Path to repository root")
    args = parser.parse_args()

    res = validate_staged(cwd=args.path, max_lines=args.max_lines)

    if args.json:
        print(json.dumps(res, indent=2))
        sys.exit(0 if res.get("valid", False) else 1)

    if "error" in res and not res.get("staged_files"):
        print(f"[ERROR] {res['error']}")
        sys.exit(1)

    print(f"=== Commit Architect Staged Diff Validation ===")
    print(f"Files staged: {res['staged_file_count']}")
    for f in res['staged_files']:
        print(f"  * {f}")
    print(f"Lines: +{res['additions']} / -{res['deletions']} (total {res['total_lines']})")

    if res['errors']:
        print("\n[ERROR] Forbidden items (Must fix before committing):")
        for err in res['errors']:
            print(f"  ! {err}")

    if res['warnings']:
        print("\n[WARN] Advisories:")
        for w in res['warnings']:
            print(f"  ? {w}")

    if res['valid'] and not res['warnings']:
        print("\n[OK] Staged diff passes all checks. Ready for commit.")
        sys.exit(0)
    elif res['valid']:
        print("\n[OK] Staged diff is valid with warnings. Review above before committing.")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
