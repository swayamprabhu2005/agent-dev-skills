#!/usr/bin/env python3
"""
detect-readme-impact.py - Project Sync Documentation Impact Detector

Analyzes git diffs and modified files to determine whether an implementation
iteration has introduced changes that require updating README.md (e.g. environment
variables, dependencies, CLI commands, or prerequisites).

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

CONFIG_PATTERNS = [
    r"\.env\.example$", r"\.env\.template$", r"config\.(json|yaml|yml|py|ts|js)$",
    r"settings\.(py|json)$", r"application\.(properties|yml)$"
]

DEPENDENCY_PATTERNS = [
    r"package\.json$", r"pyproject\.toml$", r"requirements\.txt$",
    r"Cargo\.toml$", r"go\.mod$", r"pom\.xml$", r"build\.gradle$"
]

CLI_PATTERNS = [
    r"cli\.(py|ts|js|go)$", r"commands[/\\]", r"bin[/\\]"
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

def detect_impact(cwd=None):
    code, names_out, _ = run_git(["diff", "--name-only", "HEAD"], cwd=cwd)
    if code != 0:
        # Fallback to porcelain status if HEAD does not exist (e.g. fresh repo)
        code, status_out, _ = run_git(["status", "--porcelain=v1"], cwd=cwd)
        changed_files = [line[3:].strip() for line in status_out.splitlines() if len(line) > 3]
    else:
        changed_files = [f.strip() for f in names_out.splitlines() if f.strip()]

    # Filter out README and gitignore themselves
    impacted_files = [f for f in changed_files if not f.lower().endswith("readme.md") and not f.endswith(".gitignore")]

    findings = []
    needs_update = False
    categories = set()

    for f in impacted_files:
        # Check config
        for pattern in CONFIG_PATTERNS:
            if re.search(pattern, f, re.IGNORECASE):
                needs_update = True
                categories.add("Configuration")
                findings.append({"file": f, "category": "Configuration", "reason": "Environment or configuration template modified."})
                break

        # Check dependencies
        for pattern in DEPENDENCY_PATTERNS:
            if re.search(pattern, f, re.IGNORECASE):
                needs_update = True
                categories.add("Dependencies / Setup")
                findings.append({"file": f, "category": "Dependencies / Setup", "reason": "Project dependency manifest modified."})
                break

        # Check CLI
        for pattern in CLI_PATTERNS:
            if re.search(pattern, f, re.IGNORECASE):
                needs_update = True
                categories.add("Usage / Commands")
                findings.append({"file": f, "category": "Usage / Commands", "reason": "Command-line entrypoint modified."})
                break

    # Inspect README existence
    readme_path = Path(cwd or ".") / "README.md"
    has_readme = readme_path.exists()

    return {
        "has_readme": has_readme,
        "impact_detected": needs_update or (not has_readme and len(impacted_files) > 0),
        "total_changed_files": len(impacted_files),
        "categories": sorted(list(categories)),
        "findings": findings
    }

def main():
    parser = argparse.ArgumentParser(description="Detect semantic documentation impact for Project Sync.")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--path", default=".", help="Path to repository root")
    args = parser.parse_args()

    result = detect_impact(cwd=args.path)

    if args.json:
        print(json.dumps(result, indent=2))
        sys.exit(0)

    print("=== Project Sync: README Impact Detection ===")
    print(f"README.md exists: {'Yes' if result['has_readme'] else 'No (First-Time Init Required)'}")
    print(f"Impact detected:  {'Yes' if result['impact_detected'] else 'No (Documentation remains accurate)'}")

    if result['categories']:
        print(f"Impact categories: {', '.join(result['categories'])}")

    if result['findings']:
        print("\nSignificant changes detected:")
        for item in result['findings']:
            print(f"  * [{item['category']}] {item['file']}: {item['reason']}")

    if not result['impact_detected']:
        print("\n[OK] No documentation-impacting changes detected. README.md requires no update.")

if __name__ == "__main__":
    main()
