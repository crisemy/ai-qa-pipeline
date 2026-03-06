# AI-Driven QA Pipeline

[![CI Status](https://github.com/crisemy/ai-qa-pipeline/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/crisemy/ai-qa-pipeline/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Intelligent regression testing pipeline combining traditional QA automation with data-driven insights and AI-assisted test selection.**

**Pursuit for this project**: Create CI/CD-integrated automation pipelines that reduce regression cycle time by ~40% and post-release defects by ~25% through intelligent, risk-based test selection using machine learning.

## Current Features
- FastAPI-based sample Todo API (easy to extend and break for demo purposes)
- Unit & integration tests with pytest + httpx
- End-to-end API testing with Cypress (using `cy.request`)
- Full CI pipeline with GitHub Actions: lint (Ruff), unit tests, E2E tests
- Server starts reliably in CI (Uvicorn + health check wait)

## Upcoming Features
- Historical test metrics collection (duration, pass/fail, coverage)
- Defect prediction model using NASA PROMISE datasets (Random Forest)
- Intelligent test selection: run only high-risk tests based on ML predictions
- Streamlit dashboard for before/after metrics visualization

## Tech Stack
- **Backend/API**: FastAPI, Uvicorn
- **Testing**: pytest, httpx, Cypress
- **CI/CD**: GitHub Actions
- **Future**: Pandas, scikit-learn (RandomForest), Streamlit, SQLite/CSV for metrics

## Local Setup

1. Clone the repository
   ```bash
   git clone https://github.com/crisemy/ai-qa-pipeline.git
   cd ai-qa-pipeline

2. Create and activate virtual environment
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # Linux/macOS
# or on Windows: .venv\Scripts\activate

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    pip install "uvicorn[standard]"

4. Run the API
    ```bash
    python -m uvicorn src.main:app --reload

5. Run Unit Tests
    ```bash
    python -m pytest tests/ -v

6. Run Cypress E2E tests (API)
    ```bash
    npx cypress open

## CI/CD
Every push/PR triggers GitHub Actions workflow that runs:
- Ruff linting
- pytest unit tests
- Cypress E2E tests (server auto-started)
See: .github/workflows/ci.yml

## MIT License – feel free to use, modify, and share.

crisemy@gmail.com / https://www.linkedin.com/in/cristian-gn/
Looking forward to connecting with QA, Test Automation, and AI-in-QA professionals!
Happy testing!