import { useState, FormEvent } from "react";
import ReactMarkdown from "react-markdown";
import "./App.css";
import { UploadForm } from "./components/UploadForm";

interface SummaryResponse {
  selected_lines: string[];
}

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [question, setQuestion] = useState("");
  const [summary, setSummary] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!file || !question) {
      setError("Please provide both a file and a question");
      return;
    }

    setLoading(true);
    setError("");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("question", question);

    try {
      const response = await fetch("http://localhost:8000/summarize", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to get summary");
      }

      const data: SummaryResponse = await response.json();
      setSummary(data.selected_lines);
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Mini Louie.AI</h1>

      <UploadForm
        onSubmit={handleSubmit}
        setFile={setFile}
        question={question}
        setQuestion={setQuestion}
        loading={loading}
      />

      {error && <div className="error">{error}</div>}

      {summary.length > 0 && (
        <div className="results">
          <h2>Summary</h2>
          <div className="markdown-content">
            {summary.map((line, index) => (
              <ReactMarkdown key={index}>{line}</ReactMarkdown>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
