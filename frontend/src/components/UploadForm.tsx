import { FormEvent } from "react";

interface UploadFormProps {
  onSubmit: (e: FormEvent) => Promise<void>;
  setFile: (file: File | null) => void;
  question: string;
  setQuestion: (question: string) => void;
  loading: boolean;
}

export function UploadForm({
  onSubmit,
  setFile,
  question,
  setQuestion,
  loading,
}: UploadFormProps) {
  return (
    <form onSubmit={onSubmit} className="form">
      <div className="form-group">
        <label htmlFor="file">Upload Markdown File:</label>
        <input
          type="file"
          id="file"
          accept=".md"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="question">Your Question:</label>
        <input
          type="text"
          id="question"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Enter your question..."
          required
        />
      </div>

      <button type="submit" className="submit-button" disabled={loading}>
        {loading ? "Processing..." : "Get Summary"}
      </button>
    </form>
  );
}
