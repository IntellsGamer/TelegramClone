# Telegram Web Clone (Pure Python)

A production-oriented foundation for a Telegram Web style chat application using only Python for backend and server-side rendering.

## Highlights

- FastAPI async backend + WebSocket stream endpoint.
- Jinja2-rendered Telegram-inspired web shell.
- Environment-driven feature toggles via `FeatureManager`.
- Runtime protocol auto-detection (`http/https` and `ws/wss`) using `EnvironmentDetector`.
- Async SQLAlchemy models and Alembic migration starter.
- Admin CLI for user-management tasks.
- Pytest suite for critical behavior checks.

## Project Layout

- `app/` application source
- `tests/` pytest suite
- `migrations/` alembic migration files
- `docs/` architecture and design notes
- `.env.example` configuration template

## Quickstart (No Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Feature Toggles

All major capabilities are controlled by environment variables in `.env.example`.
Disabled features are represented in the admin matrix endpoint (`GET /api/admin/features`) and can be excluded from route behavior at runtime.

## API Surface

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/verify-email`
- `WS /api/stream`
- `GET /api/chats`
- `GET /api/chats/{id}/messages`
- `POST /api/chats/{id}/messages`
- `GET /api/health`

## Admin CLI

```bash
python -m app.cli.manage deactivate-user 42
```

## Testing

```bash
pytest
```

## Notes

This repository now provides a complete modular baseline for the requested Telegram clone architecture in pure Python. It includes protocol adaptation, feature matrix controls, migrations scaffold, and test coverage for core runtime toggles.
