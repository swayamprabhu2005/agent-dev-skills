#!/usr/bin/env python3
"""
test-context-matrix.py - Context Matrix Skill Structural and Operational Test Suite

Validates:
1. Canonical manifest and YAML frontmatter integrity
2. Presence and non-emptiness of all 8 framework references
3. Framework routing accuracy across representative tasks
4. Prompt quality evaluator operational states

Author: SWAYAM KIRAN PRABHU
Part of Context Matrix
License: MIT
"""

import sys
import os
import json
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def test_manifest():
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_md = os.path.join(skill_dir, "SKILL.md")
    assert os.path.exists(skill_md), f"SKILL.md missing at {skill_md}"

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter check
    assert content.startswith("---"), "SKILL.md does not start with frontmatter"
    parts = content.split("---", 2)
    assert len(parts) >= 3, "Frontmatter not properly closed with '---'"
    frontmatter = parts[1]

    assert "name: context-matrix" in frontmatter, "Missing 'name: context-matrix' in frontmatter"
    assert "description:" in frontmatter, "Missing 'description' in frontmatter"
    assert "author: SWAYAM KIRAN PRABHU" in frontmatter, "Missing author in frontmatter"
    print("  [PASS] Canonical SKILL.md and YAML frontmatter verified.")

def test_references():
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ref_dir = os.path.join(skill_dir, "references")

    expected_refs = [
        "framework-selection.md",
        "clarity.md",
        "socrates.md",
        "anticipate.md",
        "partner.md",
        "trust.md",
        "ripple.md",
        "catch.md",
        "magic.md",
        "usage-modes.md",
        "prompt-quality-checklist.md"
    ]

    for ref in expected_refs:
        path = os.path.join(ref_dir, ref)
        assert os.path.exists(path), f"Reference document missing: {ref}"
        size = os.path.getsize(path)
        assert size > 200, f"Reference document too small/empty: {ref} ({size} bytes)"

    print(f"  [PASS] All {len(expected_refs)} reference modules verified and non-empty.")

def test_framework_selection():
    import importlib
    sf = importlib.import_module("select-framework")
    select_framework = sf.select_framework

    test_matrix = [
        ("Implement a Redis distributed lock with Lua script in TypeScript", "CLARITY"),
        ("Evaluate architecture trade-offs between monolith and microservices under 8GB memory limits", "SOCRATES"),
        ("Create an onboarding tutorial and interactive quiz for junior engineers learning SQL transactions", "ANTICIPATE"),
        ("Research and compare vector databases SQLite-vec vs Chroma with benchmark harness", "PARTNER"),
        ("Advise whether our 14-person fintech startup should adopt GraphQL or REST based on team size", "TRUST"),
        ("Perform a systematic code review and debug memory leaks in Rust threadpool", "RIPPLE"),
        ("Draft a quick release announcement email for version 2.1.0 under 150 words", "CATCH"),
        ("Create a 4-panel educational comic script about Git merge conflicts featuring Maya and DevBot", "MAGIC"),
    ]

    for task, expected_fw in test_matrix:
        result = select_framework(task)
        assert result["primary"] == expected_fw, f"Task '{task[:30]}...' expected {expected_fw}, got {result['primary']}"

    # Explicit override test
    explicit = select_framework("Random task text", explicit_fw="SOCRATES")
    assert explicit["primary"] == "SOCRATES", "Explicit framework override failed"

    print(f"  [PASS] Framework selection engine verified across {len(test_matrix)} test cases.")

def test_evaluator():
    import importlib
    ep = importlib.import_module("evaluate-prompt")
    evaluate_prompt = ep.evaluate_prompt

    # Strong prompt
    strong = """
    Context: Node.js 20 service using PostgreSQL.
    Implement an idempotent user checkout function in TypeScript.
    Input: Use the existing Prisma client in src/db.ts.
    Rules: Do not allow race conditions; must use a database transaction.
    Format: Return the full function with Jest unit tests asserting rollback on error.
    """
    res_strong = evaluate_prompt(strong)
    assert res_strong["status"] in ["READY", "READY_WITH_ASSUMPTIONS"], f"Expected READY, got {res_strong['status']}"

    # Vague prompt
    vague = "Make a website"
    res_vague = evaluate_prompt(vague)
    assert res_vague["status"] == "NEEDS_CLARIFICATION", f"Expected NEEDS_CLARIFICATION, got {res_vague['status']}"

    print("  [PASS] Prompt quality evaluator verified for READY and NEEDS_CLARIFICATION states.")

def main():
    print("Running Context Matrix Verification Suite...")
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    test_manifest()
    test_references()
    test_framework_selection()
    test_evaluator()
    print("\nALL VERIFICATION CHECKS PASSED SUCCESSFULLY (100%).")

if __name__ == "__main__":
    main()
