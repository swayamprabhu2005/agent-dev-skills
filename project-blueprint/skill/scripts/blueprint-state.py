#!/usr/bin/env python3
"""
blueprint-state.py - Project Blueprint Workflow State Manager

Manages and inspects the persistent workflow state machine file (.blueprint/state.yaml).
Supports explicit approval, version bumps, review status, and JSON output.

Author: SWAYAM KIRAN PRABHU
Part of Project Blueprint (https://github.com/swayamprabhu/project-blueprint)
License: MIT
"""

import sys
import os
import json
import argparse
import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

VALID_STATES = [
    "DRAFT",
    "READY_FOR_REVIEW",
    "CHANGES_REQUESTED",
    "APPROVED",
    "IMPLEMENTATION_READY",
    "IMPLEMENTING",
    "IMPLEMENTED"
]

DEFAULT_STATE = {
    "version": 1,
    "status": "DRAFT",
    "approved_version": None,
    "updated_at": "",
    "documents": {
        "prd": "DRAFT",
        "trd": "DRAFT",
        "ui_ux": "DRAFT",
        "backend_schema": "DRAFT",
        "app_flow": "DRAFT"
    },
    "open_questions_count": 0,
    "unresolved_conflicts": 0
}

def get_state_path(base_dir):
    # Check standard path docs/project-blueprint/.blueprint/state.yaml
    p1 = Path(base_dir) / "docs" / "project-blueprint" / ".blueprint" / "state.yaml"
    if p1.exists() or (Path(base_dir) / "docs" / "project-blueprint").exists():
        return p1
    # Fallback to .blueprint/state.yaml in current dir
    return Path(base_dir) / ".blueprint" / "state.yaml"

def parse_simple_yaml(text):
    # Lightweight YAML parser for state file (avoids external pyyaml dependency)
    data = {}
    current_dict = data
    current_key = None

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if not val:
                current_dict[key] = {}
                current_key = key
            else:
                # Type conversion
                if val.lower() == "null" or val == "~":
                    parsed_val = None
                elif val.lower() == "true":
                    parsed_val = True
                elif val.lower() == "false":
                    parsed_val = False
                elif val.isdigit():
                    parsed_val = int(val)
                else:
                    parsed_val = val.strip('"\'')

                if current_key and line.startswith("  "):
                    current_dict[current_key][key] = parsed_val
                else:
                    current_dict[key] = parsed_val
                    current_key = None
    return data

def dump_simple_yaml(data):
    lines = []
    lines.append(f"version: {data.get('version', 1)}")
    lines.append(f"status: {data.get('status', 'DRAFT')}")
    approved = data.get('approved_version')
    lines.append(f"approved_version: {approved if approved is not None else 'null'}")
    lines.append(f'updated_at: "{data.get("updated_at", "")}"')
    lines.append(f"open_questions_count: {data.get('open_questions_count', 0)}")
    lines.append(f"unresolved_conflicts: {data.get('unresolved_conflicts', 0)}")
    lines.append("documents:")
    for doc, st in data.get("documents", {}).items():
        lines.append(f"  {doc}: {st}")
    return "\n".join(lines) + "\n"

def load_state(state_file):
    if not state_file.exists():
        return None
    try:
        content = state_file.read_text(encoding="utf-8")
        parsed = parse_simple_yaml(content)
        # Merge with defaults
        res = dict(DEFAULT_STATE)
        res.update(parsed)
        return res
    except Exception as e:
        return None

def save_state(state_file, data):
    state_file.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = datetime.datetime.utcnow().isoformat() + "Z"
    text = dump_simple_yaml(data)
    state_file.write_text(text, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Manage Project Blueprint workflow state.")
    parser.add_argument("action", choices=["status", "init", "request-review", "approve", "request-changes", "start-implementation"], help="Workflow action")
    parser.add_argument("--dir", default=".", help="Base project directory")
    parser.add_argument("--json", action="store_true", help="Output state as JSON")
    args = parser.parse_args()

    state_file = get_state_path(args.dir)
    state = load_state(state_file)

    if args.action == "init":
        if state:
            print(f"[WARN] State file already exists at: {state_file}")
        else:
            state = dict(DEFAULT_STATE)
            save_state(state_file, state)
            print(f"[OK] Initialized Project Blueprint state file: {state_file}")
        return

    if not state:
        if args.json:
            print(json.dumps({"error": "No blueprint state found. Run 'init' first."}, indent=2))
        else:
            print("[ERROR] No Project Blueprint state file found. Run with 'init' to initialize.")
        sys.exit(1)

    if args.action == "request-review":
        state["status"] = "READY_FOR_REVIEW"
        for k in state.get("documents", {}):
            state["documents"][k] = "READY"
        save_state(state_file, state)
        print(f"[OK] Blueprint v{state['version']} transitioned to READY_FOR_REVIEW.")

    elif args.action == "approve":
        state["status"] = "APPROVED"
        state["approved_version"] = state["version"]
        save_state(state_file, state)
        print(f"[OK] Blueprint v{state['version']} is officially APPROVED. Implementation unlocked.")

    elif args.action == "request-changes":
        state["status"] = "CHANGES_REQUESTED"
        state["version"] += 1
        # Unset approved version until new version is approved
        save_state(state_file, state)
        print(f"[OK] State set to CHANGES_REQUESTED. Incremented blueprint version to v{state['version']}.")

    elif args.action == "start-implementation":
        if state.get("status") != "APPROVED" and state.get("status") != "IMPLEMENTATION_READY":
            print(f"[ERROR] Cannot begin implementation. Current status is '{state.get('status')}'. Explicit approval is mandatory.")
            sys.exit(1)
        state["status"] = "IMPLEMENTING"
        save_state(state_file, state)
        print(f"[OK] Status updated to IMPLEMENTING under approved blueprint v{state.get('approved_version')}.")

    if args.json:
        print(json.dumps(state, indent=2))
    else:
        print(f"\n=== Project Blueprint State ===")
        print(f"File:             {state_file}")
        print(f"Current Version:  v{state.get('version', 1)}")
        print(f"Status:           {state.get('status')}")
        print(f"Approved Version: {'v' + str(state.get('approved_version')) if state.get('approved_version') is not None else 'None (LOCKED)'}")
        print(f"Implementation:   {'UNLOCKED' if state.get('status') in ['APPROVED', 'IMPLEMENTATION_READY', 'IMPLEMENTING', 'IMPLEMENTED'] else 'BLOCKED'}")
        print("\nDocument Status:")
        for doc, st in state.get("documents", {}).items():
            print(f"  • {doc.upper():<16} [{st}]")

if __name__ == "__main__":
    main()
