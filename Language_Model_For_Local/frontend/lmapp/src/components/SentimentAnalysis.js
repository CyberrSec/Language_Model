import React, { useState } from 'react';
import './SentimentAnalysis.css';

function SentimentAnalysis() {
  const [text, setText] = useState('');
  const [sentiment, setSentiment] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Fetch the API URL and API key from environment variables
  const apiUrl = process.env.REACT_APP_API_URL;
  const apiKey = process.env.REACT_APP_API_KEY;

  const handleAnalyze = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${apiUrl}/analyze-sentiment`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey // Include API key in headers
        },
        body: JSON.stringify({ text })
      });

      const data = await response.json();
      if (response.ok) {
        setSentiment(data);
        setError('');
      } else {
        setError(data.detail || 'An error occurred while analyzing the sentiment.');
      }
    } catch (err) {
      setError('An error occurred while analyzing the sentiment.');
    }
    setLoading(false);
  };

  return (
    <div className="sentiment-analysis">
      <h2>Analyze Sentiment</h2>
      <textarea 
        value={text} 
        onChange={(e) => setText(e.target.value)} 
        placeholder="Enter text here..." 
      />
      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? 'Analyzing...' : 'Analyze'}
      </button>
      {error && <p className="error">{error}</p>}
      {sentiment && (
        <div className="result">
          <h3>Sentiment Analysis:</h3>
          {Object.entries(sentiment).map(([label, score]) => (
            label !== "overall" ? (
              <p key={label}><strong>{label.charAt(0).toUpperCase() + label.slice(1)}:</strong> {(score * 100).toFixed(2)}%</p>
            ) : (
              <p key={label}><strong>Overall Sentiment:</strong> {score}</p>
            )
          ))}
        </div>
      )}
    </div>
  );
}

export default SentimentAnalysis;
