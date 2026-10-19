#!/usr/bin/env python3
"""
evaluate-prompt.py - Context Matrix Prompt Quality Evaluator

Audits a draft prompt against the 10-point Quality Checklist:
Goal clarity, context, negative constraints, inputs, deliverables, testability, etc.
Outputs a qualitative readiness rating:
- READY: Fully specified and testable
- READY_WITH_ASSUMPTIONS: Usable, minor assumptions required
- NEEDS_CLARIFICATION: Ambiguous or missing essential constraints

Author: SWAYAM KIRAN PRABHU
Part of Context Matrix
License: MIT
"""

import sys
import json
import argparse
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def evaluate_prompt(prompt_text):
    text = prompt_text.strip()
    checks = []

    # 1. Goal Clarity
    has_action_verb = bool(re.search(r"\b(implement|create|build|refactor|design|analyze|review|explain|write|fix)\b", text, re.I))
    checks.append({
        "id": "goal_clarity",
        "name": "Goal Clarity",
        "passed": has_action_verb,
        "detail": "Contains direct action verbs." if has_action_verb else "Lacks direct action verb; deliverable is vague."
    })

    # 2. Context
    has_context = len(text.split()) >= 15 or bool(re.search(r"\b(context|we have|in our|background|running on|using|environment)\b", text, re.I))
    checks.append({
        "id": "context",
        "name": "Context Grounding",
        "passed": has_context,
        "detail": "Provides background environment or sufficient task depth." if has_context else "Lacks background context or operational environment."
    })

    # 3. Negative Constraints
    has_constraints = bool(re.search(r"\b(do not|must not|cannot|never|avoid|without|restrict|limit)\b", text, re.I))
    checks.append({
        "id": "constraints",
        "name": "Negative Constraints & Boundaries",
        "passed": has_constraints,
        "detail": "Explicitly bounds out-of-scope behaviors or restrictions." if has_constraints else "No negative constraints found; risk of unconstrained edits."
    })

    # 4. Inputs
    has_inputs = bool(re.search(r"(`[^`]+`|\bfile\b|\bcode\b|\berror\b|\btrace\b|\binput\b|\bschema\b|\bdata\b)", text, re.I))
    checks.append({
        "id": "inputs",
        "name": "Input Artifacts",
        "passed": has_inputs,
        "detail": "References input code, files, or data artifacts." if has_inputs else "No input references found; assumes agent locates inputs."
    })

    # 5. Target Output Definition
    has_output_def = bool(re.search(r"\b(return|output|format|markdown|json|table|diff|deliverable|export)\b", text, re.I))
    checks.append({
        "id": "output_def",
        "name": "Deliverable Format Definition",
        "passed": has_output_def,
        "detail": "Explicitly requests a specific format or structure." if has_output_def else "Deliverable format is implicit."
    })

    # 6. Verification & Testability
    has_verification = bool(re.search(r"\b(test|verify|benchmark|validate|assert|check|spec)\b", text, re.I))
    checks.append({
        "id": "verification",
        "name": "Verification Protocol",
        "passed": has_verification,
        "detail": "Includes verification, testing, or acceptance criteria." if has_verification else "Lacks explicit testing or verification criteria."
    })

    # 7. Conciseness / Signal-to-Noise
    word_count = len(text.split())
    has_fluff = bool(re.search(r"\b(world-class|best in class|state of the art|super clean|masterpiece)\b", text, re.I))
    checks.append({
        "id": "signal_to_noise",
        "name": "Signal-to-Noise Ratio",
        "passed": not has_fluff,
        "detail": "Free of hyperbolic marketing filler." if not has_fluff else "Contains vague hyperbolic terms ('world-class', 'masterpiece')."
    })

    passed_count = sum(1 for c in checks if c["passed"])

    if passed_count >= 6 and checks[0]["passed"]:
        status = "READY"
        summary = "Prompt is well-structured, bounded, and ready for immediate execution."
    elif passed_count >= 4 and checks[0]["passed"]:
        status = "READY_WITH_ASSUMPTIONS"
        summary = "Prompt is usable; proceeding with reasonable engineering assumptions."
    else:
        status = "NEEDS_CLARIFICATION"
        summary = "Prompt lacks essential goal clarity or input parameters; clarification recommended."

    gaps = [c["name"] + ": " + c["detail"] for c in checks if not c["passed"]]

    return {
        "status": status,
        "passed_checks": f"{passed_count}/{len(checks)}",
        "summary": summary,
        "actionable_gaps": gaps,
        "checks": checks
    }

def main():
    parser = argparse.ArgumentParser(description="Context Matrix Prompt Quality Evaluator")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt text to audit")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()
    result = evaluate_prompt(args.prompt)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Readiness Status : {result['status']}")
        print(f"Score            : {result['passed_checks']}")
        print(f"Summary          : {result['summary']}")
        if result['actionable_gaps']:
            print("\nActionable Gaps to Address:")
            for gap in result['actionable_gaps']:
                print(f"  - {gap}")

if __name__ == "__main__":
    main()
