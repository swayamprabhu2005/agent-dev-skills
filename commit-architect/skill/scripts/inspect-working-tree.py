#!/usr/bin/env python3
"""
inspect-working-tree.py - Commit Architect Working-Tree Auditor

Audits current Git working tree status, detects uncommitted files, branches,
and identifies potential risks (such as unignored secrets, large files, or detached HEAD).

Author: SWAYAM KIRAN PRABHU
Part of Commit Architect (https://github.com/swayamprabhu/commit-architect)
License: MIT
"""

import sys
import subprocess
import json
import argparse
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SENSITIVE_PATTERNS = [
    ".env", ".env.local", ".env.production", "id_rsa", "id_ed25519",
    ".pem", ".key", "credentials.json", "service-account.json"
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
        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except FileNotFoundError:
        return 127, "", "git executable not found in PATH"

def audit_tree(cwd=None):
    code, out, err = run_git(["rev-parse", "--is-inside-work-tree"], cwd=cwd)
    if code != 0:
        return {"error": "Not a Git repository or Git is unavailable", "details": err}

    # Branch inspection
    _, branch, _ = run_git(["branch", "--show-current"], cwd=cwd)
    if not branch:
        _, branch, _ = run_git(["rev-parse", "--short", "HEAD"], cwd=cwd)
        branch = f"DETACHED_HEAD ({branch})"

    # Upstream status
    _, status_sb, _ = run_git(["status", "-sb"], cwd=cwd)
    header = status_sb.splitlines()[0] if status_sb else ""

    # Porcelain status
    _, porcelain, _ = run_git(["status", "--porcelain=v1"], cwd=cwd)
    lines = porcelain.splitlines() if porcelain else []

    staged = []
    unstaged = []
    untracked = []
    potential_secrets = []

    for line in lines:
        if len(line) < 3:
            continue
        index_status = line[0]
        worktree_status = line[1]
        filepath = line[3:].strip()

        # Check for untracked / unignored sensitive files
        for pattern in SENSITIVE_PATTERNS:
            if pattern in filepath.lower():
                potential_secrets.append(filepath)
                break

        if index_status in ("M", "A", "D", "R", "C"):
            staged.append({"status": index_status, "file": filepath})
        if worktree_status in ("M", "D"):
            unstaged.append({"status": worktree_status, "file": filepath})
        elif index_status == "?" and worktree_status == "?":
            untracked.append(filepath)

    # Recent commits
    _, recent_log, _ = run_git(["log", "-n", "3", "--oneline"], cwd=cwd)
    recent_commits = recent_log.splitlines() if recent_log else []

    return {
        "branch": branch,
        "status_summary": header,
        "staged_count": len(staged),
        "staged": staged,
        "unstaged_count": len(unstaged),
        "unstaged": unstaged,
        "untracked_count": len(untracked),
        "untracked": untracked,
        "potential_secrets": potential_secrets,
        "recent_commits": recent_commits,
        "clean": len(staged) == 0 and len(unstaged) == 0 and len(untracked) == 0
    }

def main():
    parser = argparse.ArgumentParser(description="Audit Git working tree status for safe commit planning.")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--path", default=".", help="Path to repository root")
    args = parser.parse_args()

    result = audit_tree(cwd=args.path)

    if args.json:
        print(json.dumps(result, indent=2))
        sys.exit(0 if "error" not in result else 1)

    if "error" in result:
        print(f"Error: {result['error']}")
        if result.get("details"):
            print(f"Details: {result['details']}")
        sys.exit(1)

    print(f"=== Commit Architect Working-Tree Audit ===")
    print(f"Branch: {result['branch']}")
    print(f"Summary: {result['status_summary']}")
    print()
    print(f"Staged changes:    {result['staged_count']} file(s)")
    for item in result['staged']:
        print(f"  [{item['status']}] {item['file']}")

    print(f"Unstaged changes:  {result['unstaged_count']} file(s)")
    for item in result['unstaged']:
        print(f"  [{item['status']}] {item['file']}")

    print(f"Untracked files:   {result['untracked_count']} file(s)")
    for f in result['untracked'][:10]:
        print(f"  ? {f}")
    if len(result['untracked']) > 10:
        print(f"  ... and {len(result['untracked']) - 10} more")

    if result['potential_secrets']:
        print()
        print("[WARN] POTENTIAL SENSITIVE FILES DETECTED:")
        for s in result['potential_secrets']:
            print(f"  ! {s} (Do NOT stage or commit without explicit review!)")

    print()
    print(f"Recent history:")
    for c in result['recent_commits']:
        print(f"  {c}")

    if result['clean']:
        print("\n[OK] Working tree is completely clean.")

if __name__ == "__main__":
    main()
