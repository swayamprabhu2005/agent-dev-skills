# SOCRATES Framework

> **Purpose:** Plan complex technical work, systematically analyze architectural trade-offs, weigh hard resource constraints, and establish objective validation criteria before writing code.

The **SOCRATES** framework structures deep reasoning and strategic decision-making. It ensures that an AI assistant or engineering team thoroughly explores alternative architectures, evaluates practical limitations (budget, latency, hardware, dependencies), and establishes measurable success metrics.

---

## 1. The 8 Components of SOCRATES

```text
┌────────────────────────────────────────────────────────────────────────┐
│ S — Situation   : Current architectural, business, or project state    │
│ O — Objective   : Desired end-state, milestone, or capability          │
│ C — Constraints : Hardware, budget, deadlines, latency, dependencies   │
│ R — Role        : Strategic perspective (e.g., Enterprise Architect)   │
│ A — Action      : Concrete planning, design, or comparative evaluation │
│ T — Thinking    : Rigorous trade-off analysis & alternative exploration│
│ E — Evaluation  : Measurable criteria, benchmarks, & verification plan │
│ S — Summary     : Executive decision, synthesis, and phased roadmap    │
└────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

1. **S — Situation:**
   * What is the real-world operational baseline?
   * What existing technical debt, scale requirements, or legacy systems are involved?
2. **O — Objective:**
   * What concrete goal must be achieved? (e.g., "Handle 50,000 requests/sec with p99 < 15ms").
3. **C — Constraints:**
   * Real-world limits: Infrastructure budget ($/month), developer team capacity, legacy DB locks, compliance (HIPAA/GDPR), hardware memory limits (e.g. 4GB RAM edge nodes).
4. **R — Role:**
   * Expert persona responsible for balanced, un-hyped evaluation (e.g., Principal Cloud Systems Architect).
5. **A — Action:**
   * The explicit planning step: Compare 3 candidate message brokers, or design a multi-tenant database partitioning strategy.
6. **T — Thinking (Systematic Analysis):**
   * *Critical Core:* Explicitly analyze at least two opposing alternatives.
   * Weigh pros, cons, failure modes, operational complexity, and vendor lock-in.
   * *Rule:* Do not blindly praise one approach; expose hidden operational trade-offs.
7. **E — Evaluation:**
   * How will the team empirically verify that the chosen solution succeeded?
   * Load testing scenarios, unit test gates, synthetic monitors, or cost thresholds.
8. **S — Summary:**
   * Actionable recommendation, risk mitigation matrix, and step-by-step phased execution roadmap.

---

## 2. Planning vs. Execution Discipline

> [!IMPORTANT]
> **SOCRATES is a planning and reasoning framework, NOT an execution mandate.**
> An agent applying SOCRATES should never jump into generating application code or altering production infrastructure without explicit approval of the evaluated plan.

* **Step 1:** Establish Situation, Objective, and Constraints.
* **Step 2:** Formulate Thinking (alternatives & trade-offs).
* **Step 3:** Deliver Summary roadmap and Evaluation plan for human sign-off.
* **Step 4:** Only proceed to execution after human approval.

---

## 3. When to Use SOCRATES

* **Primary Use Cases:**
  * System architecture redesigns and major refactors.
  * Technology selection under strict resource/budget constraints.
  * Database migration and concurrency strategy planning.
  * Evaluating competing technical proposals.
* **When NOT to Use:**
  * Direct bug fixes or minor code edits (use **CLARITY** or **RIPPLE**).
  * Fast everyday requests or short communications (use **CATCH**).

---

## 4. Evaluation Checklist for SOCRATES Prompts

* [ ] Are real-world constraints (cost, latency, capacity) explicitly quantified?
* [ ] Does the Thinking component compare at least two viable architectural alternatives?
* [ ] Does it acknowledge edge cases and failure modes instead of assuming a happy path?
* [ ] Are success criteria measurable (benchmarks, SLAs, metrics)?
* [ ] Does the output keep planning separate from destructive execution?

---

## 5. Practical Example

### Example: Architectural Selection Under Hardware Constraints

```markdown
**Situation:** We are deploying an on-premise computer vision telemetry pipeline across 200 remote industrial edge gateways (NVIDIA Jetson Orin Nano, 8GB unified memory, intermittent 4G uplink).
**Objective:** Ingest 15 RTSP video streams per gateway, run inference at 10 FPS per stream, and buffer telemetry locally during connectivity drops without dropping frames or triggering OOM kills.
**Constraints:**
- Gateway hardware: 8GB total shared RAM (CPU + GPU).
- Max power draw: 15W per device.
- Local storage limit: 128GB NVMe SSD.
- Connectivity: 4G LTE with 500MB daily data quota per gateway.
**Role:** Principal Embedded Systems Architect.
**Action:** Evaluate three local message/buffering architectures: (1) SQLite with WAL mode, (2) Embedded RocksDB, (3) Embedded NATS JetStream.
**Thinking:**
- Analyze memory footprint, disk write amplification, crash recovery semantics, and CPU utilization under sustained 1000 msgs/sec write load.
- Compare ease of syncing buffered records upstream when 4G network resumes.
- Identify specific failure modes if NVMe storage reaches 95% capacity.
**Evaluation:**
- Memory consumption must remain < 500MB under peak write load.
- Recovery time from sudden power disruption must be < 3 seconds without database corruption.
- Bandwidth compression efficiency for upstream telemetry.
**Summary:** Provide a comparison matrix, recommended choice with rationale, and a 4-phase implementation roadmap.
```
