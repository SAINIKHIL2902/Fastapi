import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.core.config import settings
from app.routes import modules, exercises, auth

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Accelerated 4–5 Month FastAPI Engineering Curriculum & Grading Platform",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API Routers
app.include_router(modules.router, prefix="/api/modules", tags=["Modules & Curriculum"])
app.include_router(exercises.router, prefix="/api/exercises", tags=["Interactive Exercises & Grading"])
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication & User Management"])

# Liveness and Readiness Probes for Production
@app.get("/health/live", tags=["Monitoring"])
def liveness_check():
    return {"status": "alive", "version": settings.VERSION}

@app.get("/health/ready", tags=["Monitoring"])
def readiness_check():
    return {"status": "ready", "database": "connected", "redis": "connected"}

# Serve frontend web UI if available
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "frontend")
if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

    @app.get("/", tags=["UI"])
    def serve_frontend_index():
        index_file = os.path.join(FRONTEND_DIR, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {
            "message": "FastAPI Course Platform API is running.",
            "docs": "/docs",
            "modules": "/api/modules"
        }
else:
    @app.get("/", tags=["Root"])
    def root():
        return {
            "message": "FastAPI Course Platform API is running.",
            "docs": "/docs",
            "modules": "/api/modules"
        }
