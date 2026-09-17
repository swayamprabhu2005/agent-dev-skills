#!/usr/bin/env python3
"""
validate-blueprint.py - Project Blueprint Document & Mermaid Syntax Validator

Validates blueprint document completeness, required sections, and performs
syntax checks on embedded Mermaid diagrams (block diagrams, ER diagrams, sequences).

Author: SWAYAM KIRAN PRABHU
Part of Project Blueprint (https://github.com/swayamprabhu/project-blueprint)
License: MIT
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REQUIRED_DOCS = [
    "PRD.md",
    "TRD.md",
    "UI_UX.md",
    "BACKEND_SCHEMA.md",
    "APP_FLOW.md"
]

VALID_MERMAID_TYPES = [
    "flowchart", "graph", "erdiagram", "sequencediagram",
    "statediagram", "statediagram-v2", "classdiagram"
]

def find_blueprint_dir(base_dir):
    p1 = Path(base_dir) / "docs" / "project-blueprint"
    if p1.exists():
        return p1
    p2 = Path(base_dir)
    if (p2 / "PRD.md").exists():
        return p2
    return p1

def validate_mermaid_block(code_block, file_name, block_index):
    lines = code_block.strip().splitlines()
    if not lines:
        return [f"{file_name}: Empty Mermaid diagram block #{block_index}."]

    header = lines[0].strip().lower().split()[0]
    errors = []

    if not any(header.startswith(t) for t in VALID_MERMAID_TYPES):
        errors.append(f"{file_name} (block #{block_index}): Unrecognized Mermaid diagram type '{header}'. Expected one of {VALID_MERMAID_TYPES}.")

    # Check balanced quotes in lines
    for line_no, line in enumerate(lines, 1):
        if line.count('"') % 2 != 0:
            errors.append(f"{file_name} (block #{block_index}, line {line_no}): Unbalanced double quotes in Mermaid label: {line.strip()[:50]}")

    return errors

def validate_blueprint(blueprint_dir):
    errors = []
    warnings = []
    doc_stats = {}
    total_diagrams = 0

    if not blueprint_dir.exists():
        return {
            "valid": False,
            "error": f"Blueprint directory does not exist: {blueprint_dir}",
            "doc_stats": {},
            "diagram_count": 0
        }

    for doc in REQUIRED_DOCS:
        p = blueprint_dir / doc
        if not p.exists():
            errors.append(f"Missing required artifact: '{doc}'")
            continue

        content = p.read_text(encoding="utf-8", errors="replace")
        lines = content.splitlines()

        if len(lines) < 10:
            warnings.append(f"'{doc}' appears suspiciously brief ({len(lines)} lines). Ensure it contains full specification details.")

        # Extract mermaid blocks
        mermaid_blocks = re.findall(r"```mermaid\s*\n(.*?)\n```", content, re.DOTALL)
        total_diagrams += len(mermaid_blocks)

        for idx, block in enumerate(mermaid_blocks, 1):
            block_errors = validate_mermaid_block(block, doc, idx)
            errors.extend(block_errors)

        doc_stats[doc] = {
            "lines": len(lines),
            "diagrams": len(mermaid_blocks)
        }

    return {
        "valid": len(errors) == 0,
        "blueprint_dir": str(blueprint_dir),
        "doc_stats": doc_stats,
        "total_diagrams": total_diagrams,
        "errors": errors,
        "warnings": warnings
    }

def main():
    parser = argparse.ArgumentParser(description="Validate Project Blueprint document structure and Mermaid syntax.")
    parser.add_argument("--dir", default=".", help="Base directory containing blueprint documents")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    bp_dir = find_blueprint_dir(args.dir)
    res = validate_blueprint(bp_dir)

    if args.json:
        print(json.dumps(res, indent=2))
        sys.exit(0 if res.get("valid", False) else 1)

    print("=== Project Blueprint: Document & Diagram Validation ===")
    print(f"Directory: {res.get('blueprint_dir', bp_dir)}")

    if "error" in res:
        print(f"\n[ERROR] {res['error']}")
        sys.exit(1)

    print("\nArtifact Inventory:")
    for doc, stats in res['doc_stats'].items():
        print(f"  • {doc:<18} ({stats['lines']:>4} lines, {stats['diagrams']} diagram(s))")

    print(f"\nTotal Embedded Diagrams: {res['total_diagrams']}")

    if res['errors']:
        print("\n[ERROR] Syntax & Structural Violations:")
        for err in res['errors']:
            print(f"  ! {err}")

    if res['warnings']:
        print("\n[WARN] Advisories:")
        for w in res['warnings']:
            print(f"  ? {w}")

    if res['valid'] and not res['warnings']:
        print("\n[OK] All blueprint documents and embedded Mermaid diagrams are structurally valid.")
        sys.exit(0)
    elif res['valid']:
        print("\n[OK] Blueprint is valid with warnings.")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
