Backend for scraping pdf information from the repo syllabus-scraper.

**Running the Program**
1. python -m venv pymupdf-venv
2. . pymupdf-venv/bin/activate
3. python -m pip install --upgrade pip
4. pip install -r requirements.txt
5. uvicorn main:app --reload --port 8000

*If it doesn't work, try this:
1. python3 -m venv pymupdf-venv
2. . pymupdf-venv/bin/activate
3. python3 -m pip install --upgrade pip
4. pip install -r requirements.txt
5. uvicorn main:app --reload --port 8000
