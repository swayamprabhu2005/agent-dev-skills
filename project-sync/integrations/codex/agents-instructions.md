<!-- Project Sync AGENTS.md Instruction Block -->
<!-- Add this block to your project's AGENTS.md or ~/.codex/AGENTS.md -->

## Post-Implementation Project Synchronization Guidelines
After completing and validating any meaningful software implementation task:
1. Inspect git status and modified files to evaluate semantic impact on project documentation.
2. If features, setup commands, or environment variables changed, make minimal targeted edits to README.md. Do not rewrite unaffected sections.
3. If persistent generated build outputs or local caches were created, add precise, narrow rules to .gitignore. Never use .gitignore to hide temporary agent scratch files.
4. Conclude the interaction with a transparent completion summary distinguishing implemented features, documentation/gitignore sync outcomes, and validation results.
