# Example 06: Configuration Change (Redis Connection Settings)

This example illustrates synchronizing configuration documentation when an external cache dependency is introduced.

---

## 1. Implementation Change
Introduced Redis caching for session storage and rate limiting:
* Added `REDIS_URL` and `REDIS_CACHE_TTL` to `.env.example`.
* Updated `docker-compose.yml` to launch `redis:7-alpine`.
* Updated `src/config.py` to parse `REDIS_URL`.

## 2. Determination of Documentation Impact
* `README.md` documents environment variables and Docker services under `## Configuration`.
* Developers running the app locally without Docker need to know that Redis is now a dependency.
* **Decision:** Add Redis to the Prerequisites and add the new environment variables to the Configuration section.

## 3. Determination of Ignore-Rule Impact
* No new cache files created on the filesystem (Redis runs in memory/container).
* **Decision:** No changes required for `.gitignore`.

## 4. Resulting Modifications

### `README.md` (Diff):
```diff
 ## Prerequisites
 - Python 3.11+
 - PostgreSQL 15+
+- Redis 7+ (or run via `docker compose up -d redis`)

 ## Configuration
 | Key | Default | Description |
 | :--- | :--- | :--- |
 | `DATABASE_URL` | `postgresql://localhost/app` | Primary PostgreSQL connection string |
+| `REDIS_URL` | `redis://localhost:6379/0` | Redis caching and rate-limiting connection |
+| `REDIS_CACHE_TTL` | `3600` | Default cache expiration in seconds |
```

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Added Redis connection pool for session caching and rate limits
- Added redis container service in docker-compose.yml

Project synchronization:
- README.md — Updated: Added Redis to Prerequisites and documented REDIS_URL and REDIS_CACHE_TTL
- .gitignore — No changes required: Existing rules remain accurate

Validation:
- Tests: 24 passed (pytest)

Iteration complete.
```
