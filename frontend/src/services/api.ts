interface SummaryResponse {
  selected_lines: string[];
}

export async function submitMarkdownFile(
  file: File,
  question: string
): Promise<string[]> {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("question", question);

  const response = await fetch("http://localhost:8888/summarize", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Failed to get summary");
  }

  const data: SummaryResponse = await response.json();
  return data.selected_lines;
}
