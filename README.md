Backend for scraping pdf information from the repo syllabus-scraper.

**Running the Program**
Make sure inside pdf-api directory
1. python -m venv pymupdf-venv
2. . pymupdf-venv/bin/activate
3. python -m pip install --upgrade pip
4. pip install -r requirements.txt
5. uvicorn main:app --reload --port 8000

*If it doesn't work, try this:
1. python3 -m venv pymupdf-venv
2. . pymupdf-venv/bin/activate
3. python3 -m pip install --upgrade pip
4. pip install -r requirements.txt //Make sure inside pdf-api
5. uvicorn main:app --reload --port 8000

*If installing requirements.txt not found, install each requirement
manually using pip install

**Local Testing**
1. uvicorn main:app --reload --port 8000
2. http://localhost:8000/docs

**Running Using NGrok**
1. Run ngrok http 8000 in terminal
2. Get the link
