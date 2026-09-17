# Example 09: Configuration (Environment Variables & Infrastructure)

This example illustrates how configuration and infrastructure changes should be handled, staged, and sequenced.

---

## 1. The Task
"Add Redis caching configuration and configure Docker Compose for local development."

## 2. Repository State
* Python / Flask web application.
* Currently running without caching.
* Developers run services locally via `docker-compose.yml`.

## 3. Discovered Work
1. Update `docker-compose.yml` to spin up a `redis:7-alpine` container service.
2. Add `REDIS_URL` and `REDIS_CACHE_TTL` to `.env.example` and `config.py`.
3. Create `src/cache.py` initializing the Redis connection pool with graceful fallback if Redis is unavailable.
4. Add unit test asserting caching client fallback behavior in `tests/test_cache.py`.

## 4. Dependencies Between Work Units
* Docker Compose service definition and `.env.example` establish the runtime environment.
* `config.py` loads the environment variables.
* `src/cache.py` connects to the loaded configuration.
* All changes together form the foundational infrastructure milestone for caching.

## 5. Proposed Commit Plan
* **Single Cohesive Commit:**
  `Configure Redis container service and application cache client`

## 6. Implementation Sequence
1. Add redis container to `docker-compose.yml`.
2. Add default `REDIS_URL=redis://localhost:6379/0` to `.env.example` and `src/config.py`.
3. Implement `src/cache.py` with in-memory fallback for local unit tests.
4. Add tests in `tests/test_cache.py`.
5. Run tests. Verify all pass.
6. Verify staged diff: Ensure NO actual `.env` file containing private credentials is staged!
7. Commit.

## 7. Final Commit Message
```text
Configure Redis container service and application cache client

Add redis:7-alpine service to docker-compose.yml and define default
REDIS_URL in .env.example. Implement Redis connection pool in src/cache.py
with automatic graceful fallback to a null cache when REDIS_URL is unset.
```

## 8. Why These Boundaries Make Sense
* **Runnable Environment:** Anyone pulling this commit can immediately run `docker compose up` and run the application with working caching.
* **Security:** The commit explicitly updates `.env.example` while strictly keeping `.env` ignored.

## 9. What the Agent Should Avoid
* ❌ Accidental staging of `.env` or local credentials.
* ❌ Over-splitting: Making 1 commit for `docker-compose.yml`, 1 commit for `.env.example`, 1 commit for `config.py`, and 1 commit for `cache.py`.
