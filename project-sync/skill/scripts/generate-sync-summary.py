#!/usr/bin/env python3
"""
generate-sync-summary.py - Project Sync Completion Summary Formatter

Formats standardized, factual end-of-iteration completion summaries for the user,
transparently categorizing README and .gitignore synchronization outcomes.

Author: SWAYAM KIRAN PRABHU
Part of Project Sync (https://github.com/swayamprabhu/project-sync)
License: MIT
"""

import sys
import argparse
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

VALID_STATUSES = ["Updated", "No changes required", "Not applicable", "Unable to verify"]

def format_summary(implemented_items, readme_status, readme_note, gitignore_status, gitignore_note, validation_note=None):
    lines = ["Implementation complete.\n"]

    lines.append("Implemented:")
    if implemented_items:
        for item in implemented_items:
            lines.append(f"- {item}")
    else:
        lines.append("- Implementation tasks completed")
    lines.append("")

    lines.append("Project synchronization:")
    if readme_note:
        lines.append(f"- README.md — {readme_status}: {readme_note}")
    else:
        lines.append(f"- README.md — {readme_status}")

    if gitignore_note:
        lines.append(f"- .gitignore — {gitignore_status}: {gitignore_note}")
    else:
        lines.append(f"- .gitignore — {gitignore_status}")
    lines.append("")

    if validation_note:
        lines.append("Validation:")
        for v in validation_note.split(";"):
            if v.strip():
                lines.append(f"- {v.strip()}")
        lines.append("")

    lines.append("Iteration complete.")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Format Project Sync completion summary.")
    parser.add_argument("--implemented", action="append", help="Implemented feature bullet (can be repeated)")
    parser.add_argument("--readme-status", choices=VALID_STATUSES, default="No changes required")
    parser.add_argument("--readme-note", default="", help="Short description of README update or reason")
    parser.add_argument("--gitignore-status", choices=VALID_STATUSES, default="No changes required")
    parser.add_argument("--gitignore-note", default="", help="Short description of .gitignore update or reason")
    parser.add_argument("--validation", default="Build & tests passed", help="Semicolon-separated validation results")
    parser.add_argument("--json", action="store_true", help="Output as JSON object")
    args = parser.parse_args()

    summary_text = format_summary(
        implemented_items=args.implemented or ["Completed implementation task"],
        readme_status=args.readme_status,
        readme_note=args.readme_note,
        gitignore_status=args.gitignore_status,
        gitignore_note=args.gitignore_note,
        validation_note=args.validation
    )

    if args.json:
        data = {
            "implemented": args.implemented or [],
            "readme": {"status": args.readme_status, "note": args.readme_note},
            "gitignore": {"status": args.gitignore_status, "note": args.gitignore_note},
            "validation": args.validation,
            "formatted_summary": summary_text
        }
        print(json.dumps(data, indent=2))
        sys.exit(0)

    print(summary_text)

if __name__ == "__main__":
    main()
