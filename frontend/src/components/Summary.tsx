import ReactMarkdown from "react-markdown";

interface SummaryProps {
  lines: string[];
}

export function Summary({ lines }: SummaryProps) {
  if (lines.length === 0) return null;

  return (
    <div className="results">
      <h2>Summary</h2>
      <div className="markdown-content">
        {lines.map((line, index) => (
          <ReactMarkdown key={index}>{line}</ReactMarkdown>
        ))}
      </div>
    </div>
  );
}
