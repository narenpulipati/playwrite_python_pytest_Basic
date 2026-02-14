# playwrite_python_pytest_Basic


A minimal Python + Playwright + pytest starter repository.

## Features
- pytest for test running
- Playwright for browser automation (Python)
- GitHub Actions CI that installs Playwright browsers and runs tests

## Setup (local)
1. Create and activate a virtual environment:
   - python -m venv .venv
   - source .venv/bin/activate  (Linux/macOS) or .venv\Scripts\activate (Windows)

2. Install dependencies:
   - pip install -r requirements.txt

3. Install Playwright browsers:
   - playwright install --with-deps

4. Run tests:
   - pytest -q

## CI
The repository includes a GitHub Actions workflow that:
- Sets up Python
- Installs dependencies
- Installs Playwright browsers
- Runs `pytest`

## Notes
- This repository uses the `pytest-playwright` plugin (and the `playwright` package). Adjust `requirements.txt` if you prefer a different setup.
- If you need example tests using async/playwright APIs, tell me which style you prefer (sync or async).
