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

## Phase 2 — Database Layer

Steps:
- [ ] 1. Configure PostgreSQL connection string via environment variable
- [ ] 2. Implement `app/db.py` — SQLAlchemy engine, session factory, and `Base`
- [ ] 3. Implement `app/models.py` — `User`, `Item`, and `Interaction` ORM models
- [ ] 4. Add table creation on startup in `app/main.py`
- [ ] 5. Verify tables are created in the database

**Current step: 1**

---

Success criteria:
- Tables created successfully
- API can read/write data
