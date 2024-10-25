import random
from fastapi import APIRouter, UploadFile, Form, HTTPException
from ..models import SummaryResponse
from ..services.markdown_service import MarkdownProcessor

router = APIRouter()

@router.post(
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