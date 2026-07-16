# Database Migrations

This backend now uses Alembic for versioned schema management.

## Why

`Base.metadata.create_all()` is no longer used for application startup because it cannot safely manage schema evolution for an active project.

## Install dependencies

```powershell
python -m pip install -r backend\requirements.txt
```

## Common commands

Run these from the `backend` directory.

```powershell
python -m alembic upgrade head
python -m alembic revision --autogenerate -m "describe change"
python -m alembic downgrade -1
python -m alembic current
python -m alembic history
```

## Notes

- The initial migration is in `alembic/versions/20260716_0001_module2_schema.py`.
- `alembic/env.py` reads `DATABASE_URL` from `app.core.config.settings`.
- Future schema changes should be committed as new Alembic revisions before application code depends on them.
