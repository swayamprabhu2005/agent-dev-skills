# Example 03: Architectural Selection Under Hardware Constraints (SOCRATES)

---

## 1. User Invocation

```text
/context-matrix socrates We need to design a local caching and event store for edge gateways running on Raspberry Pi 4 (2GB RAM). Ingestion rate is 2,000 events/sec. Compare SQLite WAL vs Embedded RocksDB.
```

---

## 2. Framework Selected

* **Primary Framework:** `SOCRATES`
* **Selection Rationale:** Complex architectural planning weighing hardware limitations, memory boundaries, and competing technologies before execution.

---

## 3. Relevant Context & Constraints

* **Hardware:** Raspberry Pi 4 Model B (Quad-core ARM Cortex-A72, 2GB LPDDR4, MicroSD storage).
* **Workload:** 2,000 telemetry messages/sec continuous write load; intermittent offline periods up to 48 hours.
* **Constraints:** Max 250MB RAM for the database engine; preserve flash memory longevity (minimize MicroSD write amplification).

---

## 4. Resulting Prompt / Generated Workflow

```markdown
**Situation:** Deploying edge telemetry collectors on 2GB RAM Raspberry Pi 4 nodes with MicroSD storage, ingesting 2,000 JSON sensor payloads per second.
**Objective:** Select and architect an embedded storage layer that buffers up to 10M records locally during cloud outages with zero data loss.
**Constraints:**
- Maximum memory allocation: 250MB RAM.
- Storage wear: Must minimize write amplification to prevent MicroSD card failure within 2 years.
- Power failure resilience: ACID durability across unexpected power cuts without database corruption.
**Role:** Principal Embedded Systems Architect.
**Action:** Produce an architectural trade-off evaluation comparing:
1. SQLite 3 with Write-Ahead Logging (WAL) and memory-mapped I/O (`mmap_size`).
2. Embedded RocksDB (LSM-tree with tuned block cache and compactions).
**Thinking:**
- Contrast B-tree random writes (SQLite) vs LSM-tree sequential append & compaction writes (RocksDB) in the context of flash NAND wear.
- Analyze CPU utilization during peak compaction vs WAL checkpointing.
- Model crash recovery latency after abrupt power disruption.
**Evaluation:**
- Estimated Write Amplification Factor (WAF) for each engine under 2,000 writes/sec.
- Resident memory footprint under sustained 10,000-event backlog.
- Complexity of querying buffered records for cloud sync.
**Summary:**
- Comparison table across 6 engineering dimensions.
- Definitive architectural recommendation with tuned configuration parameters.
- Phased deployment and stress-testing roadmap.
```

---

## 5. Evaluation Criteria

* [x] **Resource Constraints:** Hardware memory and flash write limits explicitly quantified.
* [x] **Trade-Off Analysis:** Deep comparison of B-tree vs LSM-tree flash wear semantics.
* [x] **Planning vs Execution Separation:** Focuses on architecture recommendation without jumping into code.
* [x] **Readiness Status:** `READY`
