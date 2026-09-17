# First-Time Repository Initialization Reference Guide

This guide details how Project Sync bootstraps `README.md` and `.gitignore` when encountering a brand-new or uninitialized repository.

---

## 1. When Does First-Time Initialization Apply?

First-time initialization applies when an agent is tasked with creating a new application, scaffolding a new project, or working in an existing repository that lacks one or both of:
* `README.md`
* `.gitignore`

---

## 2. Bootstrapping `README.md`

When creating an initial `README.md`, prioritize clarity, honesty, and simplicity. Do not invent marketing fluff or document hypothetical future features.

### Standard Initial README Structure:
```markdown
# [Project Name]

> A concise one-sentence description of what this software does.

## Features
- Core feature 1
- Core feature 2

## Prerequisites
- Runtime and version requirements (e.g., Node.js 20+, Python 3.11+, Docker)

## Getting Started
\`\`\`bash
# Clone the repository
git clone <url>
cd <repo>

# Install dependencies
npm install # or poetry install, cargo build, etc.

# Setup environment
cp .env.example .env
\`\`\`

## Running the Application
\`\`\`bash
npm run dev
\`\`\`

## Running Tests
\`\`\`bash
npm test
\`\`\`

## License
[License Name]
```

### Critical Rules:
* **Only Document Verifiable Reality:** Only include commands (`npm test`, `poetry run app`) that actually exist in the repository's configuration files and have been verified.
* **No Speculative Sections:** Do not add "Roadmap", "Architecture", or "Deployment to AWS" sections unless they were explicitly built or requested.

---

## 3. Bootstrapping `.gitignore`

When creating an initial `.gitignore`, generate a **minimal, tech-stack-specific** ignore file.

### Step 1: Detect Tech Stack
Inspect the root directory:
* `package.json` → Node.js ecosystem (`node_modules/`, `dist/`, `.env`, npm logs).
* `pyproject.toml` / `requirements.txt` → Python ecosystem (`__pycache__/`, `*.pyc`, `.venv/`, `.pytest_cache/`).
* `Cargo.toml` → Rust ecosystem (`target/`).
* `go.mod` → Go ecosystem (`bin/`, `*.exe`).

### Step 2: Include Standard Environmental Guardrails
Always include local secrets and universal OS clutter:
```gitignore
# Environment & Secrets
.env
.env.local
*.pem
*.key

# Operating System Metadata
.DS_Store
Thumbs.db
```

### Strict Prohibition Against Generic Monster Templates:
Never copy a 600-line generic template containing rules for C++, Fortran, Delphi, and Visual Studio into a lightweight Python/FastAPI project. Keep `.gitignore` compact, readable, and strictly relevant.
