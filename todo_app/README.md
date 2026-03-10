# todo_app

FastAPI + SQLite application package containing the data models, schemas, database configuration, and app entry point for the Todo REST API.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package marker |
| `database.py` | SQLAlchemy engine, session factory, `Base` declarative class, and `get_db` dependency |
| `main.py` | FastAPI app entry point with lifespan hook that creates DB tables on startup |
| `models.py` | SQLAlchemy `Todo` ORM model with `id`, `title`, `description`, `done`, and `created_at` fields |
| `schemas.py` | Pydantic schemas: `TodoCreate` (request), `TodoUpdate` (partial update), `TodoResponse` (response) |
