from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import summary

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

app.include_router(summary.router)

@app.get("/")
async def read_root() -> dict:
    """Health check endpoint.
    
    Returns:
        Simple message indicating the API is running
    """
    return {"message": "Hello from Mini Louie.AI!"}