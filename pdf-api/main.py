import google.generativeai as genai
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import fitz
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def validate_json_response(text: str) -> dict:
    try:
        return json.loads(text) 
    except json.JSONDecodeError:
        cleaned = text.replace("```json", "").replace("```","").strip()
        return json.loads(cleaned)


@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with fitz.open(stream=contents, filetype="pdf") as pdf:
            raw_text = "\n".join([page.get_text() for page in pdf])

        model = genai.GenerativeModel("gemini-2.0-flash-001")

        prompt = f"""Extract this syllabus into valid JSON with the following structure:

        {{
          "course_name": "string",
          "instructor": [{{
            "name": "string",
            "email": "string"
          }}
          ],
          "office_hours": "string",
          "grading_policy": [
          {{
            "exams": "string",
            "assignments": "string",
            "participation": "string"
          }}
          ],
          "deadlines": [
            {{
              "type": "Midterm | Final | Homework | Project | Quiz | Writing",
              "date": "MM-DD-YYYY",
              "description": "string"
            }}
          ],
          "late_policy": "string"
        }}

        Only return valid JSON. Here's the syllabus:
        {raw_text[:30000]}"""
        
        response = model.generate_content(prompt)

        if not hasattr(response, "text") or not response.text:
                raise HTTPException(400, "No content in API response")

        print("GENAI RESPONSE:", response.text)
        structured_data = validate_json_response(response.text)
        return structured_data

    except Exception as e:
        raise HTTPException(500, f"Processing error: {str(e)}")

