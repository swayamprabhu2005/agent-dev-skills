# PARTNER Framework

> **Purpose:** Conduct deep, evidence-based research, evaluate competitive technologies, narrow down high-value solutions, execute proof-of-concept tests, and provide rigorous peer reviews.

The **PARTNER** framework transforms an AI assistant from a passive responder into a disciplined technical research partner. It prevents hallucinated benchmarks and ungrounded claims by demanding evidence-based inquiry, transparent citation, and structured option filtering.

---

## 1. The 7 Components of PARTNER

```text
┌────────────────────────────────────────────────────────────────────────┐
│ P — Purpose  : Core business or engineering goal driving the research  │
│ A — Audience : Technical stakeholders, decision-makers, or team leads  │
│ R — Research : Systematic evidence gathering from verified sources     │
│ T — Think    : Comparative analysis, trade-off matrix, & feasibility   │
│ N — Narrow   : Down-selection to 2–3 top contenders with clear rationale│
│ E — Execute  : Minimal proof-of-concept (PoC), benchmark, or prototype │
│ R — Review   : Retrospective audit, limitation disclosure, & next steps│
└────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

1. **P — Purpose:** What strategic decision or engineering blocker demands this investigation?
2. **A — Audience:** Who will evaluate this research? (e.g., VP of Infrastructure, Security Compliance Officer).
3. **R — Research (Evidence-Based Inquiry):**
   * Gather verified facts: Official documentation, GitHub repository health metrics (stars, active maintainers, open CVEs, release velocity), RFCs, and validated benchmarks.
   * *Rule on Grounding:* Never fabricate benchmark numbers, cloud pricing, or package features. If data is unverified or unavailable, explicitly mark it as *Unverified / Inconclusive*.
4. **T — Think:**
   * Evaluate contenders across standardized dimensions: License compliance, memory consumption, latency, community support, operational complexity, and vendor lock-in.
5. **N — Narrow:**
   * Filter out disqualified options early based on non-negotiable criteria (e.g. GPL license conflicts, lack of ARM64 support). Present the top 2–3 viable contenders.
6. **E — Execute:**
   * Produce a tangible test: A minimal reproduction snippet, containerized benchmark harness, or functional configuration.
7. **R — Review:**
   * Disclose blind spots, external risks, breaking changes in upcoming roadmaps, and final recommendation.

---

## 2. Research Integrity & Anti-Hallucination Rules

> [!CAUTION]
> **Strict Anti-Fabrication Mandate:**
> 1. Never cite non-existent papers, blog posts, or synthetic benchmarks as real facts.
> 2. Clearly distinguish between **empirical facts** (e.g., "Library X uses Apache 2.0 license as of v3.4") and **evaluative opinions** (e.g., "Library X has cleaner ergonomics").
> 3. Disclose currency: State the version numbers and date of documentation evaluated.

---

## 3. When to Use PARTNER

* **Primary Use Cases:**
  * Choosing between third-party open-source libraries or frameworks.
  * Cloud infrastructure tooling evaluations (e.g. Kafka vs Redpanda vs Pulsar).
  * Security posture and licensing compliance audits of external dependencies.
  * Multi-stage research and proof-of-concept planning.
* **When NOT to Use:**
  * Routine bug fixes within your own code (use **RIPPLE** or **CLARITY**).
  * Quick status updates or internal memos (use **CATCH**).

---

## 4. Evaluation Checklist for PARTNER Prompts

* [ ] Does the prompt define clear evaluation criteria before research starts?
* [ ] Are information sources restricted to verified, reputable channels?
* [ ] Does the Narrow phase explain why rejected alternatives were dropped?
* [ ] Is there a concrete execution artifact (PoC code, benchmark harness, config)?
* [ ] Are limitations and risks explicitly reviewed?

---

## 5. Practical Example

### Example: Selecting a Lightweight Vector Search Engine

```markdown
**Purpose:** Select an embedded vector search engine for an offline desktop electron application (Windows, macOS, Linux).
**Audience:** Lead Desktop Engineer and Security Review Board.
**Research:**
- Investigate three embedded vector libraries: (1) SQLite-vec, (2) Chroma (DuckDB/sqlite backend), (3) Faiss (C++ Python/Node bindings).
- Verify: Bundle size footprint (< 25MB), cross-compilation simplicity across x86_64 and Apple Silicon, license compatibility (MIT/Apache preferred).
- Disclose verified release versions and maintenance status. Do not invent benchmark queries/sec.
**Think:**
- Analyze installation complexity (pure prebuilt binary vs native toolchain requirements during `npm install`).
- Evaluate memory footprint when indexing 100,000 384-dimensional embeddings.
**Narrow:**
- Eliminate any library requiring a long-running background daemon process.
- Select the top 2 candidates meeting desktop bundling constraints.
**Execute:**
- Provide a working Node.js PoC script initializing the index, inserting 1,000 synthetic embeddings, and executing a cosine similarity k-NN search.
**Review:**
- Compare binary bundle size, cold startup latency, and long-term project viability.
```
