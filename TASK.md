# Current Task

## Phase 1 — Project Setup ✓ Complete

Steps:
- [x] 1. Create `app/` directory with `__init__.py`
- [x] 2. Create `app/main.py` with FastAPI app and `GET /` health endpoint
- [x] 3. Create placeholder files: `app/db.py`, `app/models.py`, `app/schemas.py`, `app/services.py`
- [x] 4. Verify API starts with `uvicorn app.main:app --reload`
- [x] 5. Confirm `GET /` returns health response
- [x] 6. Update TASK.md — mark Phase 1 complete, set Phase 2 as current

---

## Phase 2 — Database Layer ✓ Complete

Steps:
- [x] 1. Configure PostgreSQL connection string via environment variable
- [x] 2. Implement `app/db.py` — SQLAlchemy engine, session factory, and `Base`
- [x] 3. Implement `app/models.py` — `User`, `Item`, and `Interaction` ORM models
- [x] 4. Add table creation on startup in `app/main.py`
- [x] 5. Verify tables are created in the database

---

## Phase 3 — Interaction API ✓ Complete

Steps:
- [x] 1. Implement `app/schemas.py` — Pydantic request/response schemas for User, Item, Interaction
- [x] 2. Implement `app/crud.py` — create functions for User, Item, Interaction
- [x] 3. Add `POST /users` endpoint to `app/main.py`
- [x] 4. Add `POST /items` endpoint to `app/main.py`
- [x] 5. Add `POST /interactions` endpoint — validate user_id and item_id exist, rating in 0–5
- [x] 6. Manual smoke test all three endpoints via Swagger UI (`/docs`)
- [x] 7. Update TASK.md — mark Phase 3 complete, set Phase 4 as current

---

## Phase 4 — Recommendation Logic ✓ Complete

Steps:
- [x] 1. Create `scripts/seed.py` — populate the database with dummy users, items, and interactions
- [x] 2. Run `scripts/seed.py` and verify data appears in the database
- [x] 3. Implement `app/services.py` — recommendation logic (suggest items in the same category that the user hasn't interacted with)
- [x] 4. Add `GET /recommendations/{user_id}` endpoint to `app/main.py`
- [x] 5. Manual smoke test — call the endpoint for a seeded user and verify it returns items
- [x] 6. Update TASK.md — mark Phase 4 complete, set Phase 5 as current

---

## Phase 5 — Testing ✓ Complete

Steps:
- [x] 1. Setup pytest and create `tests/` directory with `conftest.py`
- [x] 2. Write unit tests for `app/services.py`
- [x] 3. Write API endpoint tests for all routes
- [x] 4. Run tests and verify all pass
- [x] 5. Update TASK.md — mark Phase 5 complete

---

## Phase 6 — Deployment

**Current step: 4**

Steps:
- [x] 1. Add `Procfile` with uvicorn start command using `$PORT`
- [x] 2. Fix `postgres://` → `postgresql://` URL rewrite in `app/db.py` for Railway compatibility
- [x] 3. Add `.pytest_cache/` to `.gitignore`
- [ ] 4. Push repo to GitHub
- [ ] 5. Create Railway project, connect GitHub repo, add PostgreSQL plugin
- [ ] 6. Set `DATABASE_URL` env var in Railway (auto-provided by the PostgreSQL plugin)
- [ ] 7. Run `python -m scripts.seed` via Railway console to populate demo data
- [ ] 8. Verify the public URL works — hit `/docs` and `/recommendations/{user_id}`
- [ ] 9. Update TASK.md — mark Phase 6 complete

---

Success criteria:
- All tests pass ✓
- API accessible at a public Railway URL
