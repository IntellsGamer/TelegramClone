# Architecture Decisions

- **Backend**: FastAPI with async SQLAlchemy and WebSockets.
- **Feature management**: Env-driven toggles centralized in `FeatureManager`.
- **Protocol awareness**: `EnvironmentDetector` computes http/https and ws/wss with reverse-proxy support.
- **Frontend rendering**: Jinja2 templates + minimal JS for websocket interaction.
- **Scalability plan**: Redis-backed presence/event fanout and Celery/arq for async jobs.
