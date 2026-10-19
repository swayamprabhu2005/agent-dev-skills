# Example 05: Creating Educational Documentation (ANTICIPATE)

---

## 1. User Invocation

```text
/context-matrix anticipate Write an onboarding tutorial for new engineers explaining how our repo's event-driven Kafka consumer handles dead-letter queues and poison pill retries.
```

---

## 2. Framework Selected

* **Primary Framework:** `ANTICIPATE`
* **Selection Rationale:** Technical training and developer onboarding guide designed around learner empathy and comprehension verification.

---

## 3. Relevant Context & Constraints

* **Audience:** Newly hired backend software engineers with basic microservice background, but unfamiliar with event-driven failure modes (poison pill messages, partition starvation).
* **Format:** 15-minute hands-on tutorial with diagrams, real code walkthrough, and a broken-message simulation exercise.

---

## 4. Resulting Prompt / Generated Workflow

```markdown
**Audience:** Junior to mid-level engineers joining the platform team. Familiar with REST and basic Kafka topics, but new to consumer offset commit strategies and Dead Letter Queues (DLQ).
**Need:** Understand how to write resilient Kafka consumers in TypeScript that isolate unparseable messages into a DLQ without halting partition processing.
**Task:** Author an interactive 15-minute developer onboarding guide: "Resilient Kafka Message Processing & DLQ Architecture".
**Information:** Consumer offsets, commit intervals, poison pill payloads, exponential backoff retries, and DLQ routing.
**Constraints:** Reading time < 12 minutes; must use our repository's existing Kafka client wrapper (`src/kafka/consumer.ts`).
**Illustrate:** Provide an ASCII sequence diagram showing:
1. Normal message flow.
2. Transient error flow (retry 3x with backoff).
3. Permanent failure flow (forward to DLQ topic and commit consumer offset).
**Plan:**
- Part 1: The Danger of the "Poison Pill" (how one bad JSON payload halts an entire consumer group).
- Part 2: The 3-Tier Retry Architecture (In-memory retry → Retry topic → Dead letter topic).
- Part 3: Code Walkthrough (`handleIncomingEvent()` pattern).
- Part 4: Hands-on Debugging Exercise.
**Act:** Provide a realistic code snippet containing an unhandled exception that causes infinite consumer loops, with step-by-step instructions to refactor it with a DLQ producer.
**Test:** Include 3 conceptual check-for-understanding questions and a unit test asserting that an invalid schema triggers DLQ emission.
**Enhance:** Provide alerting best practices (CloudWatch metrics on DLQ message count > 0) and replay runbooks.
```

---

## 5. Evaluation Criteria

* [x] **Pedagogical Structure:** Progresses from intuitive failure mode to architecture, code, and active practice.
* [x] **Comprehension Verification:** Includes check questions and unit test assertions.
* [x] **Readiness Status:** `READY`
