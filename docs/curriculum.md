# 🚀 Accelerated FastAPI Engineering Curriculum (4–5 Months)
> **Simulating ~3 Years of Production Experience through Intensive, Hands-on Systems Engineering**

---

## 📑 Curriculum Overview
- **Duration:** 20–22 Weeks (~4.5 Months)
- **Commitment:** 25–35 Hours / Week
- **Target Outcome:** Mid/Senior Backend & AI Systems Engineer capable of designing, building, securing, observing, and scaling distributed Python systems.
- **Core Philosophy:** $\text{WHAT} \rightarrow \text{WHY} \rightarrow \text{CODE} \rightarrow \text{BREAK} \rightarrow \text{DEBUG} \rightarrow \text{TEST} \rightarrow \text{DEPLOY} \rightarrow \text{OBSERVE}$.

---

## 🗺️ Week-by-Week Roadmap

### 📦 Phase 1: Core Foundations & Modern Python (Weeks 1–3)
#### Week 1: Python Type Hints, Asyncio Event Loop & ASGI
- **Concepts:** Python 3.11+ type system, `typing.Annotated`, coroutines vs threads, GIL, ASGI specification vs WSGI, Uvicorn uvloop.
- **Hands-on:** Build an asynchronous HTTP client script using `httpx` that fetches 100 endpoints concurrently without thread blocking.
- **Failure Mode Lab:** Intentionally run a heavy CPU-bound loop inside an `async def` route; observe event loop starvation and latency explosion.

#### Week 2: Request & Response Contracts with Pydantic V2
- **Concepts:** Pydantic models, field validators (`@field_validator`), serialization schemas, response models to eliminate sensitive data leakage.
- **Hands-on:** Build strict request validation pipelines with custom regex validation, nested models, and OpenAPI doc customization.
- **Failure Mode Lab:** Send invalid payloads in Postman and inspect why FastAPI interceptor generates HTTP 422 Unprocessable Entity.

#### Week 3: Routing Architecture, Radix Trees & Dependency Injection
- **Concepts:** APIRouter modularization, Radix tree route matching, `fastapi.Depends`, yield dependencies with cleanup/resource teardown.
- **Deliverable:** **Project A — Production Todo & Task Management CRUD API** with SQLite, Pydantic V2, automated Pytest suite, and full Swagger docs.

---

### 🗄️ Phase 2: Relational Modeling, Async ORMs & Migrations (Weeks 4–6)
#### Week 4: PostgreSQL Architecture & Async SQLAlchemy 2.0
- **Concepts:** Connection pooling (QueuePool), async sessions, transactional ACID guarantees, Declarative Base, ORM vs Core queries.
- **Hands-on:** Connect FastAPI to PostgreSQL using `asyncpg`; implement the repository pattern separating database queries from business logic.
- **Failure Mode Lab:** Simulate connection pool starvation; trigger and fix `QueuePool limit reached` errors under concurrent load.

#### Week 5: Database Migrations with Alembic
- **Concepts:** Schema versioning, revision history, autogenerate limitations, offline vs online migrations, non-destructive migration strategies.
- **Hands-on:** Generate revisions, downgrade and upgrade schemas, add composite indexes to production tables with zero data loss.
- **Review Checkpoint:** Ensure no raw DDL statements run without rollback migrations.

#### Week 6: Query Optimization & Indexing Internals
- **Concepts:** B-Tree indexes, Sequential Scan vs Index Scan, `EXPLAIN (ANALYZE, BUFFERS)`, N+1 query problem, eager loading (`joinedload` vs `selectinload`).
- **Deliverable:** **Project B — Task Manager API with PostgreSQL + Alembic**, query execution plans under 5ms for 500,000 records.

---

### 🔐 Phase 3: Authentication, Authorization & Security Hardening (Weeks 7–9)
#### Week 7: Password Hashing & JWT Token Lifecycle
- **Concepts:** Salting & hashing (bcrypt/argon2), JWT structure (Header, Payload, Signature), short-lived access tokens + long-lived refresh tokens.
- **Hands-on:** Build user registration, login, token refresh, and logout endpoints with token blacklisting in Redis.
- **Failure Mode Lab:** Tamper with JWT signature bits and verify backend returns HTTP 401 Unauthorized.

#### Week 8: Role-Based Access Control (RBAC) & OAuth2 Flows
- **Concepts:** Scopes, permissions hierarchy (Admin, Editor, Viewer), custom dependency injection for route authorization guards.
- **Hands-on:** Build declarative security decorators: `@require_permission("orders:write")`.
- **Review Checkpoint:** Prevent Insecure Direct Object References (IDOR) on all user resource endpoints.

#### Week 9: API Security Defenses (CORS, Rate Limiting, Input Sanitization)
- **Concepts:** OWASP Top 10 API Security, CORS policy, sliding-window rate limiting via Redis token bucket, SQL injection defenses.
- **Deliverable:** **Project C — Multi-Tenant Auth & Billing Service** with JWT, refresh tokens, RBAC permissions, and Redis rate limiting.

---

### ⚙️ Phase 4: Asynchronous Task Queues & Background Workers (Weeks 10–12)
#### Week 10: Background Tasks & Asynchronous Workers
- **Concepts:** FastAPI `BackgroundTasks` (ephemeral) vs Celery / Dramatiq (distributed, durable), Redis / RabbitMQ brokers.
- **Hands-on:** Dispatch asynchronous image processing and transactional email generation to worker processes.
- **Failure Mode Lab:** Crash a worker process mid-execution; observe task acknowledgment (`ack_late`) and automatic task redelivery.

#### Week 11: Scheduled Jobs, Retries & Idempotency
- **Concepts:** Celery Beat, Exponential backoff with jitter, Idempotency keys (`Idempotency-Key` header) to prevent duplicate charges.
- **Hands-on:** Implement idempotent API endpoints storing completed request hashes in Redis.
- **Review Checkpoint:** Ensure every external network call (Stripe, Email API) has explicit timeout and retry limits.

#### Week 12: File Processing & Object Storage Pipelines
- **Concepts:** Streaming file uploads, chunked transfer encoding, direct-to-S3 pre-signed URLs, background virus scanning.
- **Deliverable:** **Project D — Resilient Asynchronous Media Processing Pipeline** with Celery, Redis, and idempotency guarantees.

---

### 🌐 Phase 5: Microservices, Events & Distributed Systems (Weeks 13–15)
#### Week 13: Service Decomposition & Event-Driven Architecture
- **Concepts:** Monolith decomposition patterns, Synchronous HTTP vs Asynchronous Messaging, Domain-Driven Design (DDD).
- **Hands-on:** Split into User Service and Order Service communicating via RabbitMQ event exchanges.
- **Failure Mode Lab:** Bring down the User Service; observe Order Service buffering events without dropping transactions.

#### Week 14: Outbox Pattern & Event Sourcing
- **Concepts:** Dual-write problem, Transactional Outbox Pattern, Debezium CDC (Change Data Capture), exactly-once semantics.
- **Hands-on:** Implement an outbox table within Postgres to guarantee atomic state changes and event dispatch.
- **Review Checkpoint:** Validate schema versioning for events with JSON Schema / Avro.

#### Week 15: Distributed Resiliency (Circuit Breakers & Retries)
- **Concepts:** Circuit breaker pattern, Fallbacks, Service discovery, Contract testing with Pact.
- **Deliverable:** **Project E — Event-Driven Order Processing Microservices** with RabbitMQ, outbox pattern, and circuit breakers.

---

### ⚡ Phase 6: Real-Time Systems, WebSockets & Streaming (Weeks 16–17)
#### Week 16: Asynchronous WebSockets & Bidirectional Communication
- **Concepts:** WebSocket handshake, full-duplex communication, connection managers, heartbeat pings.
- **Hands-on:** Build a live real-time notification gateway handling 5,000 active concurrent WebSocket clients.
- **Failure Mode Lab:** Disconnect clients abruptly; verify server reclaims file descriptors without socket leakage.

#### Week 17: Distributed Pub/Sub & Streaming Responses
- **Concepts:** Scaling WebSockets across multiple nodes with Redis Pub/Sub, Server-Sent Events (SSE) for real-time LLM token streaming.
- **Hands-on:** Build a streaming AI chat endpoint returning tokens from an LLM as they generate.
- **Review Checkpoint:** Benchmark WebSocket connection capacity using Locust load tests.

---

### 📊 Phase 7: Observability, Metrics, Tracing & Production Hardening (Weeks 18–19)
#### Week 18: Structured Logging & Prometheus Metrics
- **Concepts:** Correlation IDs (`X-Request-ID`), structured JSON logging (`structlog`), RED metrics (Rate, Errors, Duration).
- **Hands-on:** Instrument FastAPI with Prometheus client; export P90/P99 latency histograms and error rate gauges to Grafana.
- **Failure Mode Lab:** Inject 500ms database latency; watch P99 latency spikes trigger automated alerting rules.

#### Week 19: Distributed Tracing with OpenTelemetry & Sentry
- **Concepts:** Context propagation (W3C tracecontext), Spans, Jaeger distributed trace viewer, Sentry error tracking.
- **Hands-on:** Trace an HTTP request as it traverses FastAPI $\rightarrow$ PostgreSQL $\rightarrow$ Redis $\rightarrow$ External API.
- **Review Checkpoint:** Confirm 100% of uncaught exceptions generate Sentry alerts with stack trace and request metadata.

---

### 🚀 Phase 8: Cloud, Infrastructure-as-Code, CI/CD & Capstone (Weeks 20–22)
#### Week 20: Production Containerization & CI/CD Pipelines
- **Concepts:** Multi-stage Docker builds (<120MB image), distroless/slim base images, non-root user execution, GitHub Actions matrix tests.
- **Hands-on:** Build an automated CI/CD pipeline running linters (`ruff`, `mypy`), pytest suites, and vulnerability scans (`trivy`).

#### Week 21: Infrastructure as Code (Terraform / Cloud Deployment)
- **Concepts:** VPCs, Subnets, ECS / EKS or DigitalOcean App Platform, AWS Secrets Manager, managed RDS Postgres, Redis caching.
- **Hands-on:** Provision production cloud infrastructure with reproducible Terraform modules.

#### Week 22: Complete Capstone Defense & Deployment
- **Deliverable:** **Project F — Enterprise-Grade Production SaaS / AI Inference Platform**:
  - Live deployed cloud URL
  - GitHub Actions CI/CD with zero-downtime rolling updates
  - Distributed tracing & Prometheus/Grafana monitoring dashboard
  - Full OpenAPI documentation and test coverage > 85%.

---

## 🏆 The 6 Progressively Complex Projects

| Project | Name | Weeks | Tech Stack | Key Architectural Focus |
| :--- | :--- | :---: | :--- | :--- |
| **A** | Todo & Notes CRUD API | 1–3 | FastAPI, Pydantic V2, SQLite, Pytest, HTTPX | Clean architecture, type safety, OpenAPI specs |
| **B** | Relational Task Manager | 4–6 | FastAPI, PostgreSQL, SQLAlchemy 2.0, Alembic | Async connection pools, migrations, B-Tree index optimization |
| **C** | Multi-Tenant Auth & Billing | 7–9 | FastAPI, JWT, Refresh Tokens, Redis, RBAC | Security, password hashing, IDOR prevention, rate limiting |
| **D** | Media Processing Pipeline | 10–12 | FastAPI, Celery, Redis, S3 Pre-signed URLs | Durable task queues, exponential retries, idempotency keys |
| **E** | Event-Driven Microservices | 13–15 | FastAPI, RabbitMQ, Docker Compose, Outbox Pattern | Service decoupling, circuit breakers, message schemas |
| **F** | Enterprise Capstone SaaS | 20–22 | Full Stack + Terraform + CI/CD + OTel + Grafana | Production deployment, telemetry, zero-downtime releases |

---

## 📝 Grading Rubric & Review Checklist
- **Functionality (40%):** Meets all acceptance criteria, handles edge cases, returns proper HTTP status codes.
- **Code Quality & Architecture (25%):** Follows repository pattern, strict type hints, zero lint errors (`ruff`), clean modularization.
- **Automated Tests (20%):** Unit and integration test coverage > 80%, tested against real databases using testcontainers.
- **Documentation & OpenAPI (10%):** Interactive Swagger docs, clear README with local and Docker reproduction steps.
- **Observability & Security (5%):** Health probes (`/health/live`, `/health/ready`), structured logging, and non-root Docker execution.
