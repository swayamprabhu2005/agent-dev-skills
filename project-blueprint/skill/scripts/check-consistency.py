#!/usr/bin/env python3
"""
check-consistency.py - Project Blueprint Cross-Document Consistency Auditor

Audits the five blueprint documents for requirement ID coverage (REQ-xxx),
unresolved open questions (OPEN-xxx), assumptions (ASSUM-xxx), and cross-document alignment.

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

def find_blueprint_dir(base_dir):
    p1 = Path(base_dir) / "docs" / "project-blueprint"
    if p1.exists():
        return p1
    p2 = Path(base_dir)
    if (p2 / "PRD.md").exists():
        return p2
    return p1

def audit_consistency(blueprint_dir):
    missing_docs = []
    doc_contents = {}

    for doc in REQUIRED_DOCS:
        doc_path = blueprint_dir / doc
        if not doc_path.exists():
            missing_docs.append(doc)
        else:
            doc_contents[doc] = doc_path.read_text(encoding="utf-8", errors="replace")

    if missing_docs:
        return {
            "valid": False,
            "error": f"Missing required blueprint document(s): {', '.join(missing_docs)}",
            "missing_docs": missing_docs,
            "requirements": [],
            "open_questions": [],
            "assumptions": []
        }

    # Extract requirement IDs from PRD.md
    prd_text = doc_contents["PRD.md"]
    req_ids = sorted(list(set(re.findall(r"\bREQ-\d+\b", prd_text))))

    # Track coverage across other 4 documents
    coverage = {}
    for req in req_ids:
        coverage[req] = {
            "TRD.md": req in doc_contents["TRD.md"],
            "UI_UX.md": req in doc_contents["UI_UX.md"],
            "BACKEND_SCHEMA.md": req in doc_contents["BACKEND_SCHEMA.md"],
            "APP_FLOW.md": req in doc_contents["APP_FLOW.md"]
        }

    # Extract Open Questions and Assumptions across all files
    all_text = "\n".join(doc_contents.values())
    open_questions = sorted(list(set(re.findall(r"\bOPEN-\d+\b", all_text))))
    assumptions = sorted(list(set(re.findall(r"\bASSUM-\d+\b", all_text))))

    # Check for CONFLICT markers
    conflicts_found = re.findall(r"CONFLICT\s+DETECTED", all_text, re.IGNORECASE)

    warnings = []
    for req, doc_map in coverage.items():
        missing_in = [d for d, present in doc_map.items() if not present]
        if len(missing_in) == 4:
            warnings.append(f"{req} is defined in PRD.md but not referenced in any technical or design specification.")

    if open_questions:
        warnings.append(f"There are {len(open_questions)} unresolved open question(s): {', '.join(open_questions)}")

    is_valid = len(conflicts_found) == 0 and len(missing_docs) == 0

    return {
        "valid": is_valid,
        "blueprint_dir": str(blueprint_dir),
        "total_requirements": len(req_ids),
        "requirement_ids": req_ids,
        "coverage": coverage,
        "open_questions_count": len(open_questions),
        "open_questions": open_questions,
        "assumptions_count": len(assumptions),
        "assumptions": assumptions,
        "conflicts_count": len(conflicts_found),
        "warnings": warnings
    }

def main():
    parser = argparse.ArgumentParser(description="Check consistency across Project Blueprint documents.")
    parser.add_argument("--dir", default=".", help="Base directory containing blueprint documents")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    bp_dir = find_blueprint_dir(args.dir)
    res = audit_consistency(bp_dir)

    if args.json:
        print(json.dumps(res, indent=2))
        sys.exit(0 if res.get("valid", False) else 1)

    print("=== Project Blueprint: Consistency Audit ===")
    print(f"Directory: {res.get('blueprint_dir', bp_dir)}")

    if "error" in res:
        print(f"\n[ERROR] {res['error']}")
        sys.exit(1)

    print(f"\nRequirements Found: {res['total_requirements']}")
    for req in res['requirement_ids']:
        docs_present = [d.replace('.md', '') for d, ok in res['coverage'][req].items() if ok]
        cov_str = ", ".join(docs_present) if docs_present else "None"
        print(f"  • {req}: Referenced in [{cov_str}]")

    print(f"\nAssumptions Logged:  {res['assumptions_count']} ({', '.join(res['assumptions']) if res['assumptions'] else 'None'})")
    print(f"Open Questions:      {res['open_questions_count']} ({', '.join(res['open_questions']) if res['open_questions'] else 'None'})")

    if res['conflicts_count'] > 0:
        print(f"\n[ERROR] {res['conflicts_count']} explicit conflict marker(s) detected. Resolve before review!")
        sys.exit(1)

    if res['warnings']:
        print("\n[WARN] Advisories:")
        for w in res['warnings']:
            print(f"  ? {w}")

    if res['valid']:
        print("\n[OK] All 5 blueprint artifacts exist and pass consistency checks.")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
