import React, { useState } from 'react';
import './Summarize.css';

function Summarize() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Fetch the API URL and API key from environment variables
  const apiUrl = process.env.REACT_APP_API_URL;
  const apiKey = process.env.REACT_APP_API_KEY;

  const handleSummarize = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${apiUrl}/summarize`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey // Include API key in headers
        },
        body: JSON.stringify({ text })
      });

      const data = await response.json();
      if (response.ok) {
        setSummary(data.summary);
        setError('');
      } else {
        setError(data.detail || 'An error occurred while summarizing the text.');
      }
    } catch (err) {
      setError('An error occurred while summarizing the text.');
    }
    setLoading(false);
  };

  return (
    <div className="summarize">
      <h2>Summarize Text</h2>
      <textarea 
        value={text} 
        onChange={(e) => setText(e.target.value)} 
        placeholder="Enter text here..." 
      />
      <button onClick={handleSummarize} disabled={loading}>
        {loading ? 'Summarizing...' : 'Summarize'}
      </button>
      {error && <p className="error">{error}</p>}
      {summary && (
        <div className="result">
          <h3>Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default Summarize;
