# Generic Agent & Tooling Integration for Chroma-Craft

Chroma-Craft is platform-agnostic and runs in any AI agent framework that supports tools or instructions (LangChain, AutoGen, CrewAI, LlamaIndex, custom LLM loops).

## Integration Protocol
1. **System Prompt Injection:** Point your agent system prompt to `skill/SKILL.md`.
2. **Tool Execution:** Expose the scripts in `skill/scripts/` (`palette-generator.py`, `wcag-checker.py`, `token-exporter.py`) as CLI tool calls.
3. **Verification:** Instruct the agent to run `wcag-checker.py` before finalizing any UI palette recommendations.
