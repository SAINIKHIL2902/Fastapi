import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_checks():
    """Verify liveness and readiness monitoring endpoints"""
    live_res = client.get("/health/live")
    assert live_res.status_code == 200
    assert live_res.json()["status"] == "alive"

    ready_res = client.get("/health/ready")
    assert ready_res.status_code == 200
    assert ready_res.json()["status"] == "ready"

def test_modules_listing():
    """Verify curriculum modules are listed"""
    res = client.get("/api/modules/")
    assert res.status_code == 200
    data = res.json()
    assert "modules" in data
    assert len(data["modules"]) >= 8

def test_module_details_and_exercises():
    """Verify retrieving module 1 and its exercises"""
    res = client.get("/api/modules/m01")
    assert res.status_code == 200
    mod = res.json()
    assert mod["id"] == "m01"
    assert "exercises" in mod

    ex_res = client.get("/api/modules/m01/exercises")
    assert ex_res.status_code == 200
    exercises = ex_res.json()
    assert len(exercises) >= 2

def test_auth_signup_and_login():
    """Verify student registration and JWT login flow"""
    email = "sai_student_test@example.com"
    password = "SuperSecurePassword123!"

    # Signup
    signup_res = client.post("/api/auth/signup", json={
        "name": "Sai Nikhil",
        "email": email,
        "password": password
    })
    assert signup_res.status_code == 201
    assert "access_token" in signup_res.json()

    # Login
    login_res = client.post("/api/auth/login", json={
        "email": email,
        "password": password
    })
    assert login_res.status_code == 200
    assert "access_token" in login_res.json()

def test_exercise_automated_grading():
    """Verify the automated code runner grades a valid exercise submission with 100 score"""
    valid_code = """
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy", "code": 200}
"""
    res = client.post("/api/exercises/ex01/submit", json={
        "code": valid_code
    })
    assert res.status_code == 200
    result = res.json()
    assert result["status"] == "passed"
    assert result["score"] == 100
