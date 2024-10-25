from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
import random
import re

class SummaryResponse(BaseModel):
    selected_lines: List[str] = Field(
        description="Selected lines from the markdown file",
        min_items=1,
        max_items=10
    )

class MarkdownProcessor:
    """Handles processing and cleaning of markdown content."""
    
    @staticmethod
    def clean_line(line: str) -> str:
        """Remove markdown syntax from a line of text.
        
        Args:
            line: A string containing markdown syntax
            
        Returns:
            Cleaned string with common markdown elements removed
        """
        return re.sub(
            r"(\#|\*|\[.*?\]\(.*?\)|\!\[.*?\]\(.*?\))", 
            "", 
            line.strip()
        )
    
    @staticmethod
    def extract_valid_lines(content: str) -> List[str]:
        """Extract and clean non-empty lines from markdown content.
        
        Args:
            content: Raw markdown content as string
            
        Returns:
            List of cleaned, non-empty lines
        """
        lines = content.splitlines()
        return [
            MarkdownProcessor.clean_line(line) 
            for line in lines 
            if line.strip()
        ]

app = FastAPI(
    title="Mini Louie.AI",
    description="A markdown file summarization API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/summarize", 
    response_model=SummaryResponse,
    description="Summarize a markdown file by selecting random lines"
)
async def summarize_file(
    file: UploadFile, 
    question: str = Form()
) -> SummaryResponse:
    """Process a markdown file and return a random selection of lines.
    
    Args:
        file: Uploaded markdown file
        question: User's question (currently unused, for future ML implementation)
        
    Returns:
        SummaryResponse containing selected lines
        
    Raises:
        HTTPException: If file is empty or cannot be decoded
    """
    try:
        content = await file.read()
        lines = MarkdownProcessor.extract_valid_lines(content.decode())

        if not lines:
            raise HTTPException(
                status_code=400, 
                detail="The file is empty or has no valid content."
            )

        # Select random lines (1-10)
        random_num_lines = random.randint(1, min(10, len(lines)))
        selected_lines = random.sample(lines, random_num_lines)

        return SummaryResponse(selected_lines=selected_lines)

    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400, 
            detail="Unable to read the file. Make sure it is a valid Markdown file."
        )

@app.get("/")
async def read_root() -> dict:
    """Health check endpoint.
    
    Returns:
        Simple message indicating the API is running
    """
    return {"message": "Hello from Mini Louie.AI!"}