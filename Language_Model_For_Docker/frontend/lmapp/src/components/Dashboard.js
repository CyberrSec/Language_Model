import React from 'react';
import { Link } from 'react-router-dom';
import './Dashboard.css';

function Dashboard() {
  return (
    <div className="dashboard">
      <h1>LinguaAI Dashboard</h1>
      <div className="cards">
        <Link to="/summarize" className="card">
          <i className="fas fa-compress-alt"></i>
          <h2>Summarize Text</h2>
          <p>Condense long texts into concise summaries</p>
        </Link>
        <Link to="/analyze-sentiment" className="card">
          <i className="fas fa-smile-beam"></i>
          <h2>Analyze Sentiment</h2>
          <p>Determine the emotional tone of your text</p>
        </Link>
      </div>
    </div>
  );
}

export default Dashboard;