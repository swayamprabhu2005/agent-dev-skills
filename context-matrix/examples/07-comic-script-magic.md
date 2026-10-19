# Example 07: Generating a Creative Artifact (MAGIC)

---

## 1. User Invocation

```text
/context-matrix magic Create a 4-panel educational webcomic script illustrating the concept of "Premature Optimization" in software engineering.
```

---

## 2. Framework Selected

* **Primary Framework:** `MAGIC`
* **Selection Rationale:** Creative narrative deliverable requiring character continuity, visual staging, comedic timing, and educational takeaway.

---

## 3. Relevant Context & Constraints

* **Theme:** Donald Knuth's adage: "Premature optimization is the root of all evil".
* **Tone:** Relatable, witty developer humor; lighthearted self-deprecation.
* **Continuity Constraints:** Characters must have consistent physical traits and distinct visual signatures across all 4 panels.

---

## 4. Resulting Prompt / Generated Workflow

```markdown
**Motivation:** Illustrate the comedic trap where an engineer spends 3 days shaving 4 microseconds off a string formatting function in a CLI tool that runs once a week, while ignoring a 10-second blocking database query.
**Audience:** Software developers, computer science students, tech Twitter/Mastodon community.
**Goal:** Deliver a sharp, funny reminder to profile real bottlenecks before optimizing micro-operations.
**Input:**
- Protagonist 1 (Sam): Enthusiastic junior developer, oversized yellow hoodie, round wireframe glasses, perpetually surrounded by floating profiling graphs.
- Protagonist 2 (Alex): Pragmatic senior developer, dark grey turtleneck, holding a steaming coffee mug labeled "grep".
- Visual Style: Clean modern webcomic line art, 4-panel 2x2 grid.
**Create:**
A complete 4-panel script detailing:
- **Panel 1 (The Eureka Moment):**
  * Visual: Sam staring intensely at an IDE with wild excitement, pointing to a function labeled `formatUserName()`.
  * Sam: "Alex! I rewrote our name-formatter in hand-rolled inline assembly! It is now 12 nanoseconds faster per call!"
  * Alex: (Sipping coffee, unimpressed expression) "Great. How often is that called?"
- **Panel 2 (The Scale):**
  * Visual: Medium shot of Sam proudly pulling up the production cron schedule.
  * Sam: "Every Sunday at 3:00 AM! Once!"
  * SFX: *tumbleweed rolling across server rack*
- **Panel 3 (The Reality):**
  * Visual: Wide angle showing the customer checkout screen spinning with a giant loading wheel labeled "Connecting to database... 14.8s".
  * Alex: (Pointing to the customer checkout screen) "Meanwhile, the payment gateway is doing an unindexed table scan of 80 million rows."
  * Sound Effect: *slow grinding gears*
- **Panel 4 (The Punchline):**
  * Visual: Sam now typing furiously, completely ignoring the database screen.
  * Sam: "If I convert the assembly to binary opcodes, I might get another 2 nanoseconds!"
  * Alex: (Facepalm, steam rising from coffee mug)
  * Caption Box at bottom: "Profile before you polish."
```

---

## 5. Evaluation Criteria

* [x] **Creative Structure:** Crisp 4-panel staging with visual directions, dialogue, and comedic escalation.
* [x] **Character Consistency:** Specific visual anchors (yellow hoodie, wireframe glasses, grey turtleneck) defined for continuity.
* [x] **Readiness Status:** `READY`
