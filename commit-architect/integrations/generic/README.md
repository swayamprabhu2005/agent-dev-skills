# Generic Agent Skills Integration

Commit Architect is designed from the ground up to adhere to the open **Agent Skills** specification ([agentskills.io](https://agentskills.io)).

Any AI coding platform, IDE extension, or autonomous agent runner that implements the open specification can load Commit Architect without modification.

---

## Specification Conformance

Commit Architect complies with the open specification:

1. **Manifest & Entry Point:** Rooted at `SKILL.md` containing standardized YAML frontmatter:
   ```yaml
   ---
   name: commit-architect
   description: >-
     Architect clean, logical Git commit histories for software engineering tasks.
   license: MIT
   metadata:
     author: SWAYAM KIRAN PRABHU
     version: 0.1.0
   ---
   ```
2. **Progressive Disclosure:** Token efficiency is preserved by separating detailed operational manuals into `references/` and deterministic checks into `scripts/`.
3. **Vendor Neutrality:** The core skill instructions are strictly written in third-person imperative (`"The agent should..."`) and make zero vendor-proprietary assumptions.

---

## Universal Installation

If your agent runtime looks for skills in a standard path (such as `.agents/skills/` or `.skills/`):

```bash
# Link the canonical skill folder into your agent's configured skills directory:
mkdir -p .skills
ln -s /path/to/commit-architect/skill .skills/commit-architect
```

If your platform does not yet support dynamic skill discovery, you can point your system prompt or project-level instructions to load `skill/SKILL.md` directly.
