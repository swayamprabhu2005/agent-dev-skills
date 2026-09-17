#!/usr/bin/env python3
"""
verify-commit.py - Commit Architect Message Verifier

Validates commit messages against natural developer standards and repository rules.
Detects vague subjects, AI buzzwords, unsolicited AI trailers, and formatting flaws.

Author: SWAYAM KIRAN PRABHU
Part of Commit Architect (https://github.com/swayamprabhu/commit-architect)
License: MIT
"""

import sys
import argparse
import json
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

VAGUE_SUBJECTS = [
    r"^wip\b",
    r"^update(s)?\b",
    r"^update(d)?\s+files\b",
    r"^changes\b",
    r"^fix(es)?\b",
    r"^fix\s+bug(s)?\b",
    r"^fix\s+stuff\b",
    r"^misc\b",
    r"^various\s+(fixes|improvements|updates)\b",
    r"^work\s+in\s+progress\b",
    r"^clean\s*up\b"
]

AI_BUZZWORDS = [
    r"\bcomprehensive\b",
    r"\brobust\b",
    r"\bseamless(ly)?\b",
    r"\bmeticulous(ly)?\b",
    r"\belevate\b",
    r"\bholistic\b",
    r"\bsynergistic\b"
]

AI_TRAILERS = [
    r"co-authored-by:\s*ai\b",
    r"co-authored-by:.*<.*bot.*>",
    r"generated\s+(by|with)\s+(ai|chatgpt|claude|gemini|antigravity|copilot)",
    r"ai-generated"
]

CONVENTIONAL_PREFIX_RE = r"^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([a-zA-Z0-9_\-\./]+\))?!?: .+"

def verify_message(message_text, conventional_mode=False):
    lines = message_text.strip().splitlines()
    if not lines or not lines[0].strip():
        return {"valid": False, "errors": ["Commit message is completely empty."]}

    subject = lines[0].strip()
    errors = []
    warnings = []

    # 1. Subject line length
    if len(subject) > 72:
        warnings.append(f"Subject line exceeds 72 characters ({len(subject)} chars). Keep subject concise.")

    # 2. Capitalization (for natural mode)
    if not conventional_mode:
        if subject and not subject[0].isupper() and not subject.startswith("`"):
            warnings.append(f"Subject line should begin with a capital letter: '{subject}'")

    # 3. Trailing period
    if subject.endswith("."):
        errors.append("Subject line should not end with a period.")

    # 4. Blank line after subject if body exists
    if len(lines) > 1:
        if lines[1].strip() != "":
            errors.append("There must be a blank line between the subject line and the commit body.")

    # 5. Vague subject detection
    for pattern in VAGUE_SUBJECTS:
        if re.search(pattern, subject, re.IGNORECASE):
            errors.append(f"Subject is overly vague and does not convey meaningful software intent: '{subject}'")
            break

    # 6. Conventional commit mode check
    has_conventional_prefix = bool(re.match(CONVENTIONAL_PREFIX_RE, subject))
    if conventional_mode:
        if not has_conventional_prefix:
            errors.append("Repository requires Conventional Commits format (e.g., 'feat: ...' or 'fix(scope): ...').")
    else:
        if has_conventional_prefix:
            warnings.append(
                f"Conventional commit prefix detected ('{subject.split(':')[0]}:'). "
                "Commit Architect defaults to natural developer language unless the repository explicitly mandates Conventional Commits."
            )

    # 7. AI buzzwords check
    full_text = "\n".join(lines)
    for pattern in AI_BUZZWORDS:
        matches = re.findall(pattern, full_text, re.IGNORECASE)
        if matches:
            warnings.append(f"Avoid generic AI buzzwords ({', '.join(set(matches))}). Use direct, technical descriptions.")

    # 8. Unsolicited AI trailer check
    for pattern in AI_TRAILERS:
        if re.search(pattern, full_text, re.IGNORECASE):
            warnings.append("AI attribution trailer detected. Only include AI attribution if explicitly mandated by the repository.")

    return {
        "valid": len(errors) == 0,
        "subject": subject,
        "body_lines": len(lines) - 2 if len(lines) > 2 else 0,
        "errors": errors,
        "warnings": warnings
    }

def main():
    parser = argparse.ArgumentParser(description="Verify a Git commit message for Commit Architect compliance.")
    parser.add_argument("-m", "--message", help="Commit message string to verify")
    parser.add_argument("-f", "--file", help="Path to commit message file (e.g., .git/COMMIT_EDITMSG)")
    parser.add_argument("--conventional", action="store_true", help="Enforce Conventional Commits mode (if required by repo)")
    parser.add_argument("--json", action="store_true", help="Output validation as JSON")
    args = parser.parse_args()

    content = ""
    if args.message:
        content = args.message
    elif args.file:
        try:
            with open(args.file, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except OSError as e:
            print(f"Error reading file {args.file}: {e}")
            sys.exit(1)
    else:
        if not sys.stdin.isatty():
            content = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(1)

    result = verify_message(content, conventional_mode=args.conventional)

    if args.json:
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["valid"] else 1)

    print("=== Commit Architect Message Verification ===")
    print(f"Subject: {result.get('subject', '')}")

    if result["errors"]:
        print("\n[ERROR] Issues to resolve:")
        for err in result["errors"]:
            print(f"  ! {err}")

    if result["warnings"]:
        print("\n[WARN] Advisories:")
        for w in result["warnings"]:
            print(f"  ? {w}")

    if result["valid"] and not result["warnings"]:
        print("\n[OK] Commit message is natural, concise, and professional.")
        sys.exit(0)
    elif result["valid"]:
        print("\n[OK] Commit message is acceptable with warnings.")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
