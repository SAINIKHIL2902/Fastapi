import json
import os
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

router = APIRouter()

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "curriculum_data.json")

def load_curriculum_data() -> Dict[str, Any]:
    if not os.path.exists(DATA_PATH):
        raise HTTPException(status_code=500, detail="Curriculum dataset not found.")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@router.get("/")
def list_modules():
    """Lists all 22 weeks of accelerated course modules"""
    data = load_curriculum_data()
    return data["curriculum"]

@router.get("/{module_id}")
def get_module(module_id: str):
    """Retrieves a specific module by ID (e.g. m01, m02)"""
    data = load_curriculum_data()
    for m in data["curriculum"]["modules"]:
        if m["id"] == module_id:
            return m
    raise HTTPException(status_code=404, detail=f"Module '{module_id}' not found.")

@router.get("/{module_id}/exercises")
def get_module_exercises(module_id: str):
    """Lists hands-on coding exercises for a specific module"""
    module = get_module(module_id)
    return module.get("exercises", [])
