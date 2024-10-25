from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random
import re

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SummaryResponse(BaseModel):
    selected_lines: List[str]

@app.post("/summarize", response_model=SummaryResponse)
async def summarize_file(file: UploadFile, question: str = Form()):
    try:
        content = await file.read()
        lines = content.decode().splitlines()

        lines = [re.sub(r"(\#|\*|\[.*?\]\(.*?\)|\!\[.*?\]\(.*?\))", "", line.strip()) for line in lines if line.strip()]

        if not lines:
            raise HTTPException(status_code=400, detail="The file is empty or has no valid content.")

        random_num_lines = random.randint(1, min(10, len(lines)))
        selected_lines = random.sample(lines, random_num_lines)

        return SummaryResponse(selected_lines=selected_lines)

    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Unable to read the file. Make sure it is a valid Markdown file.")

@app.get("/")
async def read_root():
    return {"message": "Hello from Mini Louie.AI!"}