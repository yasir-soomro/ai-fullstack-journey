# FastAPI Backend

FastAPI framework learning and application development.

## Structure

- **`01_fastapi/`** - Active FastAPI project
  - `main.py` - FastAPI application entry point
  - `pyproject.toml` - Project dependencies and configuration
  - `uv.lock` - Dependency lock file
  - `.python-version` - Python version specification

## Getting Started

### Prerequisites

- Python 3.10+
- UV package manager (or pip)

### Installation

```bash
cd 01_fastapi
uv sync
# or
pip install -r requirements.txt
```

### Running the Application

```bash
cd 01_fastapi
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Learning Path

1. Start with basic route creation (`GET /`)
2. Learn about request/response models
3. Implement CRUD operations
4. Add middleware and dependencies
5. Handle errors and validation

