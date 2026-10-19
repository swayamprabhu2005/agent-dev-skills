#!/usr/bin/env python3
"""
select-framework.py - Context Matrix Framework Selection Engine

Analyzes task descriptions and determines the optimal prompt-engineering framework
among the 8 Context Matrix frameworks (CLARITY, SOCRATES, ANTICIPATE, PARTNER, TRUST, RIPPLE, CATCH, MAGIC).

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

FRAMEWORKS = {
    "CLARITY": {
        "name": "CLARITY",
        "description": "General software engineering, precise functional specs, coding, technical implementation.",
        "keywords": [
            (r"\bimplement(ation)?\b", 2), (r"\bwrite code\b", 2), (r"\bfunction\b", 1), (r"\bapi\b", 1),
            (r"\btypescript\b", 1), (r"\bpython\b", 1), (r"\brust\b", 1), (r"\bclass\b", 1),
            (r"\bmodule\b", 1), (r"\brefactor(ing)?\b", 2), (r"\bschema\b", 1), (r"\bdatabase\b", 1),
            (r"\bendpoint\b", 1), (r"\binterface\b", 1), (r"\bfeature\b", 1), (r"\bcode\b", 1)
        ]
    },
    "SOCRATES": {
        "name": "SOCRATES",
        "description": "System architecture, trade-off analysis, feasibility, hardware/budget constraints, roadmaps.",
        "keywords": [
            (r"\barchitect(ural|ure)?\b", 2), (r"\btrade-?offs?\b", 3), (r"\bfeasibility\b", 3),
            (r"\bhardware limits?\b", 3), (r"\bhardware\b", 1), (r"\bbudget\b", 2), (r"\blatency\b", 1),
            (r"\bthroughput\b", 1), (r"\bscale\b", 1), (r"\bcompare architectures\b", 3),
            (r"\bdesign system\b", 2), (r"\broadmap\b", 2), (r"\bmonolith(ic)?\b", 2),
            (r"\bmicroservices\b", 2), (r"\bconcurrency model\b", 2)
        ]
    },
    "ANTICIPATE": {
        "name": "ANTICIPATE",
        "description": "Tutorials, educational guides, developer onboarding, exercises, comprehension checks.",
        "keywords": [
            (r"\btutorial\b", 3), (r"\bguide\b", 2), (r"\bonboarding\b", 3), (r"\bteach\b", 2),
            (r"\blearn(ing)?\b", 2), (r"\bbeginner\b", 2), (r"\bstudent\b", 2), (r"\bpedagogy\b", 3),
            (r"\bexercises?\b", 2), (r"\bquiz(zes)?\b", 3), (r"\bdocumentation\b", 1),
            (r"\bwalkthrough\b", 2), (r"\bcourse\b", 2), (r"\bworkshop\b", 2)
        ]
    },
    "PARTNER": {
        "name": "PARTNER",
        "description": "Deep research, library/tool evaluations, empirical benchmarks, proof-of-concept tests.",
        "keywords": [
            (r"\bresearch\b", 3), (r"\bevaluate tools?\b", 3), (r"\bcompare (libraries|tools|databases)\b", 3),
            (r"\bbenchmark(s)?\b", 3), (r"\bproof of concept\b", 3), (r"\bpoc\b", 3),
            (r"\btechnology selection\b", 3), (r"\bcompetitors\b", 2), (r"\bvendor\b", 1),
            (r"\bopen source\b", 1), (r"\bcve\b", 2), (r"\blicense compliance\b", 2)
        ]
    },
    "TRUST": {
        "name": "TRUST",
        "description": "Tailored decision support, situational advisory, executive recommendations, trade-off reasoning.",
        "keywords": [
            (r"\badvise\b", 3), (r"\brecommend(ation)?\b", 3), (r"\bdecision\b", 2), (r"\btailor(ed)?\b", 3),
            (r"\bconsult(ing)?\b", 2), (r"\bwhich should (we|i)\b", 3), (r"\bstrategy\b", 2),
            (r"\bpros and cons\b", 2), (r"\bsituation\b", 1), (r"\bstartup\b", 2), (r"\bteam size\b", 3)
        ]
    },
    "RIPPLE": {
        "name": "RIPPLE",
        "description": "Systematic code review, root-cause debugging, dataset audit, security vulnerability scan.",
        "keywords": [
            (r"\bcode reviews?\b", 3), (r"\breview(ing)?\b", 2), (r"\bdebug(ging)?\b", 3),
            (r"\bdiagnos(e|is|tic)\b", 3), (r"\bcrash(es)?\b", 3), (r"\bstack ?trace\b", 3),
            (r"\bpanics?\b", 3), (r"\bleaks?\b", 3), (r"\baudit(ing)?\b", 3), (r"\bvulnerabilit(y|ies)\b", 3),
            (r"\bdataset\b", 2), (r"\bdata quality\b", 3), (r"\broot cause\b", 3), (r"\berror\b", 1)
        ]
    },
    "CATCH": {
        "name": "CATCH",
        "description": "Everyday requests, release notes, concise announcements, short scripts, quick summaries.",
        "keywords": [
            (r"\bquick\b", 2), (r"\bshort\b", 2), (r"\beveryday\b", 2), (r"\brelease notes?\b", 3),
            (r"\bannouncement\b", 3), (r"\bemail\b", 2), (r"\bslack\b", 2), (r"\bmemo\b", 2),
            (r"\bchangelog\b", 3), (r"\bbrief\b", 2), (r"\bshell script\b", 2), (r"\bone-?liner\b", 2)
        ]
    },
    "MAGIC": {
        "name": "MAGIC",
        "description": "Creative deliverables, narrative storytelling, comic scripts, marketing copy, video scripts.",
        "keywords": [
            (r"\bcreative\b", 2), (r"\bstory\b", 2), (r"\bcomics?\b", 3), (r"\bscript\b", 2),
            (r"\billustration\b", 3), (r"\bvideo\b", 2), (r"\bpanels?\b", 3), (r"\bmarketing\b", 2),
            (r"\blanding page\b", 2), (r"\bhumor\b", 2), (r"\bmetaphor\b", 2), (r"\bfiction\b", 2),
            (r"\bhero section\b", 2)
        ]
    }
}

def score_task(task_text):
    text_lower = task_text.lower()
    scores = {}
    for fw_key, fw_info in FRAMEWORKS.items():
        score = 0
        matches = []
        for pattern, weight in fw_info["keywords"]:
            match_list = re.findall(pattern, text_lower)
            if match_list:
                score += len(match_list) * weight
                matches.append(pattern.replace(r"\b", "").replace("?", "").replace("(ing)", "").replace("s?", ""))
        scores[fw_key] = {"score": score, "matches": matches}
    return scores

def select_framework(task_text, explicit_fw=None):
    if explicit_fw:
        fw_upper = explicit_fw.upper()
        if fw_upper in FRAMEWORKS:
            return {
                "primary": fw_upper,
                "secondary": None,
                "reason": f"Explicit framework '{fw_upper}' requested by user.",
                "scores": {}
            }
        else:
            return {
                "error": f"Unknown framework '{explicit_fw}'. Valid options: {list(FRAMEWORKS.keys())}"
            }

    scores = score_task(task_text)
    sorted_fws = sorted(scores.items(), key=lambda item: item[1]["score"], reverse=True)

    top_fw, top_data = sorted_fws[0]
    runner_up_fw, runner_up_data = sorted_fws[1]

    # Default fallback to CLARITY if no keywords matched
    if top_data["score"] == 0:
        return {
            "primary": "CLARITY",
            "secondary": None,
            "reason": "Default fallback to CLARITY for general technical instructions.",
            "scores": {k: v["score"] for k, v in scores.items()}
        }

    # Evaluate potential multi-framework combination
    secondary = None
    if runner_up_data["score"] >= 2 and (top_data["score"] - runner_up_data["score"]) <= 1:
        # Check known complementary pairs
        valid_pairs = {
            ("SOCRATES", "RIPPLE"), ("CLARITY", "RIPPLE"), ("ANTICIPATE", "MAGIC"),
            ("PARTNER", "SOCRATES"), ("CATCH", "CLARITY")
        }
        candidate_pair = tuple(sorted([top_fw, runner_up_fw]))
        for p1, p2 in valid_pairs:
            if candidate_pair == tuple(sorted([p1, p2])):
                secondary = runner_up_fw
                break

    return {
        "primary": top_fw,
        "secondary": secondary,
        "reason": f"Matched intent keywords: {', '.join(top_data['matches'][:4])}.",
        "scores": {k: v["score"] for k, v in scores.items()}
    }

def main():
    parser = argparse.ArgumentParser(description="Context Matrix Framework Selection Engine")
    parser.add_argument("--task", type=str, default="", help="Task description to analyze")
    parser.add_argument("--framework", type=str, default=None, help="Explicitly requested framework")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    if not args.task and not args.framework:
        parser.print_help()
        sys.exit(1)

    result = select_framework(args.task, args.framework)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if "error" in result:
            print(f"Error: {result['error']}")
            sys.exit(1)
        print(f"Primary Framework  : {result['primary']}")
        if result['secondary']:
            print(f"Secondary Framework: {result['secondary']}")
        print(f"Rationale          : {result['reason']}")

if __name__ == "__main__":
    main()
