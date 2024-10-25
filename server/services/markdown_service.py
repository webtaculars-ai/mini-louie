import re
from typing import List

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
        # Remove headers, bold/italic, links, and images
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