import os
import json
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.services.runner import code_runner

router = APIRouter()

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "curriculum_data.json")

class CodeSubmission(BaseModel):
    code: str
    user_id: Optional[str] = "student-01"

# Verification tests mapped to exercise IDs
TEST_HARNESSES = {
    "ex01": """
# Test Exercise 1: Verify health endpoint
import asyncio
from fastapi.testclient import TestClient

client = TestClient(app)
response = client.get("/health")
assert response.status_code == 200, f"Expected 200, got {response.status_code}"
assert response.json().get("status") == "healthy", "Expected status='healthy'"
""",
    "ex02": """
# Test Exercise 2: Verify Pydantic user validation
from fastapi.testclient import TestClient

client = TestClient(app)
# Test valid submission
res_valid = client.post("/users", json={"email": "alice@example.com", "age": 22})
assert res_valid.status_code in [200, 201], f"Expected 201/200, got {res_valid.status_code}"

# Test invalid age (must be >= 18)
res_invalid = client.post("/users", json={"email": "bob@example.com", "age": 16})
assert res_invalid.status_code == 422, f"Expected 422 for age < 18, got {res_invalid.status_code}"
""",
    "ex03": """
# Test Exercise 3: Async database session
import asyncio

async def test_session():
    async for session in get_db():
        assert session is not None, "Session should not be None"
        break

asyncio.run(test_session())
""",
    "ex04": """
# Test Exercise 4: JWT token creation
token = create_access_token({"sub": "user_123"}, expires_minutes=15)
assert isinstance(token, str) and len(token) > 20, "Generated token is invalid"
decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
assert decoded["sub"] == "user_123", "Decoded subject mismatch"
"""
}

def find_exercise(ex_id: str) -> Optional[Dict[str, Any]]:
    if not os.path.exists(DATA_PATH):
        return None
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    for m in data["curriculum"]["modules"]:
        for ex in m.get("exercises", []):
            if ex["id"] == ex_id:
                return ex
    return None

@router.get("/{exercise_id}")
def get_exercise_details(exercise_id: str):
    """Get exercise details, instructions, and starter code"""
    ex = find_exercise(exercise_id)
    if not ex:
        raise HTTPException(status_code=404, detail=f"Exercise '{exercise_id}' not found.")
    return ex

@router.post("/{exercise_id}/submit")
def submit_exercise(exercise_id: str, submission: CodeSubmission):
    """
    Submits code for automated grading and returns execution results.
    """
    ex = find_exercise(exercise_id)
    if not ex:
        raise HTTPException(status_code=404, detail=f"Exercise '{exercise_id}' not found.")

    test_assertions = TEST_HARNESSES.get(exercise_id, "assert True")
    
    # Execute code inside safety harness
    evaluation = code_runner.execute_code(
        code=submission.code,
        test_assertions=test_assertions,
        timeout_sec=5
    )

    return {
        "exercise_id": exercise_id,
        "status": evaluation["status"],
        "score": evaluation["score"],
        "stdout": evaluation["stdout"],
        "stderr": evaluation["stderr"],
        "exit_code": evaluation["exit_code"]
    }
