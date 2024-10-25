import { useState, FormEvent } from "react";
import { UploadForm } from "./components/UploadForm";
import { Summary } from "./components/Summary";
import { ErrorMessage } from "./components/ErrorMessage";
import { submitMarkdownFile } from "./services/api";
import "./App.css";

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

    try {
      const lines = await submitMarkdownFile(file, question);
      setSummary(lines);
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

      <ErrorMessage message={error} />
      <Summary lines={summary} />
    </div>
  );
}

export default App;
