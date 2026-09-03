# ⚡ FastAPI Accelerated Engineering Platform (4–5 Months)

> **Compress ~3 Years of Production Experience into 20–22 Weeks of Deep Hands-on Systems Engineering**

Welcome to the **FastAPI Accelerated Engineering Platform**. This repository contains the complete curriculum, automated grading test harness, backend API services, and interactive web dashboard designed to take you from foundational Python APIs to distributed microservices, streaming, and production cloud systems.

---

## 🗺️ The 22-Week Accelerated Roadmap

| Module | Weeks | Focus Area | Capstone Deliverable |
| :--- | :---: | :--- | :--- |
| **01** | Weeks 1–3 | ASGI, Concurrency, Pydantic V2 & Dependency Injection | **Project A:** Todo & Task REST API |
| **02** | Weeks 4–6 | PostgreSQL, Async SQLAlchemy 2.0 & Alembic Migrations | **Project B:** Relational Task Manager |
| **03** | Weeks 7–9 | OAuth2, JWT Lifecycle, RBAC & Security Hardening | **Project C:** Multi-Tenant Auth & Billing Service |
| **04** | Weeks 10–12| Celery Task Queues, Redis Workers & Idempotency | **Project D:** Resilient Media Processing Pipeline |
| **05** | Weeks 13–15| Event-Driven Microservices, RabbitMQ & Outbox Pattern | **Project E:** Order Processing Microservices |
| **06** | Weeks 16–17| Real-Time WebSockets & LLM Token Streaming (SSE) | **Project E+:** Notification Gateway & Chatbot |
| **07** | Weeks 18–19| OpenTelemetry Distributed Tracing & Prometheus Metrics | Observability & Grafana Stack |
| **08** | Weeks 20–22| Terraform IaC, Multi-Stage Docker & GitHub Actions CI | **Project F:** Enterprise Capstone SaaS Platform |

> 📖 **Full syllabus and project specifications:** See [`docs/curriculum.md`](docs/curriculum.md).

---

## 🛠️ Repository Architecture

```
Fastapi/
├── backend/
│   ├── app/
│   │   ├── core/         # Settings (pydantic-settings) & Security (JWT, bcrypt)
│   │   ├── routes/       # API routers: /api/modules, /api/exercises, /api/auth
│   │   ├── services/     # Subprocess automated code grading runner with timeouts
│   │   ├── data/         # Curriculum & exercise JSON database
│   │   └── main.py       # FastAPI application entrypoint & static file mounts
│   ├── tests/            # Automated test suite (pytest + TestClient)
│   ├── requirements.txt  # Python package dependencies
│   └── Dockerfile        # Multi-stage container running as non-root (1001)
├── frontend/             # Interactive course dashboard & in-browser code sandbox
│   ├── index.html
│   ├── style.css
│   └── app.js
├── infra/
│   └── docker-compose.yml # PostgreSQL 15, Redis 7, and FastAPI backend
└── docs/
    └── curriculum.md     # Complete 20-22 week accelerated curriculum syllabus
```

---

## 🚀 Quickstart Guide

### Option 1: Run with Local Virtual Environment (Recommended for Development)

```bash
# 1. Navigate to backend
cd backend

# 2. Create isolated virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start development server
uvicorn app.main:app --reload --port 8000
```

Once running:
- 🌐 **Interactive Web Dashboard & Exercise Sandbox:** [http://localhost:8000/](http://localhost:8000/)
- 📖 **Interactive OpenAPI / Swagger Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
- 🏥 **Health Check:** [http://localhost:8000/health/live](http://localhost:8000/health/live)

---

### Option 2: Run with Docker Compose (Production-Grade Stack)

To boot the full stack with **PostgreSQL 15**, **Redis 7**, and the **FastAPI backend**:

```bash
cd infra
docker compose up --build
```

---

## 🧪 Running Automated Tests

Run the test suite to verify endpoints, authentication, and the automated code grading runner:

```bash
cd backend
source .venv/bin/activate
pytest tests/
```

---

## 🔒 Security & Git Configuration
- Sensitive personal tokens are kept strictly in `github_token.txt` and ignored by Git via `.gitignore`.
- This repository is isolated under your personal GitHub profile:
  `https://github.com/SAINIKHIL2902/Fastapi`
