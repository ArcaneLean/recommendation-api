# Recommendation API – Project Plan

## Project Goal

Build a backend service that recommends items to users based on past interactions.

The system should expose a REST API that allows:
- recording user interactions with items
- retrieving recommendations for a user

The focus of this project is **backend system design**, not complex ML models.

---

# Architecture Overview

Stack:
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

High-level components:

API Layer
- FastAPI endpoints

Service Layer
- recommendation logic
- interaction processing

Data Layer
- PostgreSQL database
- SQLAlchemy models

---

# Project Structure

recommendation-api/
    app/
        main.py
        models.py
        schemas.py
        services.py
        db.py

---

# Development Phases

## Phase 1 — Project Setup

Goal: working development environment and basic API.

Tasks:
- [ ] Create project structure
- [ ] Setup FastAPI application
- [ ] Add development dependencies
- [ ] Run API locally

Success criteria:
- API runs with `uvicorn`
- `/` endpoint returns health message

---

## Phase 2 — Database Layer

Goal: persist users, items, and interactions.

Tasks:
- [ ] Setup PostgreSQL connection
- [ ] Add SQLAlchemy models
    - User
    - Item
    - Interaction
- [ ] Create database initialization

Success criteria:
- Tables created successfully
- API can read/write data

---

## Phase 3 — Interaction API

Goal: record user interactions.

Endpoints:
- `POST /users`
- `POST /items`
- `POST /interactions`

Tasks:
- [ ] Create Pydantic schemas
- [ ] Implement CRUD endpoints
- [ ] Add basic validation

Success criteria:
- Users/items/interactions can be created through API.

---

## Phase 4 — Recommendation Logic

Goal: return recommended items for a user.

Endpoint:
- `GET /recommendations/{user_id}`

Possible approaches:
- simple heuristic (same category)
- popularity-based
- collaborative filtering (optional)

Tasks:
- [ ] Implement recommendation service
- [ ] Connect endpoint to service

Success criteria:
- API returns recommended items.

---

## Phase 5 — Testing

Goal: ensure reliability.

Tasks:
- [ ] Add unit tests for services
- [ ] Add API endpoint tests
- [ ] Setup pytest

Success criteria:
- tests run successfully.

---

## Phase 6 — Deployment (Optional)

Goal: deploy the API.

Tasks:
- [ ] Create Dockerfile
- [ ] Configure environment variables
- [ ] Deploy to cloud service

Success criteria:
- API accessible online.

