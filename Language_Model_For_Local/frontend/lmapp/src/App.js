import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Summarize from './components/Summarize';
import SentimentAnalysis from './components/SentimentAnalysis';
import Navbar from './components/Navbar';
import './App.css';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="content">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/summarize" element={<Summarize />} />
          <Route path="/analyze-sentiment" element={<SentimentAnalysis />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
