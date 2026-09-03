# ⚡ FastAPI Hands-on Engineering Lab

Welcome to your isolated FastAPI workspace.

## 🚀 Recommended Isolated Setup (Virtual Environment)
To ensure everything stays strictly isolated within this project folder without installing any packages globally on your system:

```bash
# 1. Navigate to this directory
cd "/Users/sainikhilreddy/Documents/my own files/Fastapi"

# 2. Create a local virtual environment
python3 -m venv .venv

# 3. Activate the virtual environment
source .venv/bin/activate

# 4. Install FastAPI and Uvicorn inside the environment
pip install "fastapi[standard]"
```

---

## 📁 Learning Modules Outline
- **Module 01**: Minimal GET & POST endpoints with Uvicorn
- **Module 02**: Pydantic models & request validation
- **Module 03**: Path & query parameters
- **Module 04**: Error handling (HTTPException & 422 errors)
- **Module 05**: Dependency Injection (`Depends`)
- **Module 06**: Database integration with PostgreSQL & SQLAlchemy
- **Module 07**: Automated testing with `pytest` & `httpx`
- **Module 08**: Multi-stage Docker deployment
