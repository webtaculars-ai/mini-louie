from pydantic import BaseModel, Field
from typing import List

class SummaryResponse(BaseModel):
    selected_lines: List[str] = Field(
        description="Selected lines from the markdown file",
        min_items=1,
        max_items=10
    )