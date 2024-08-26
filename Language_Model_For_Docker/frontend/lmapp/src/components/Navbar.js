import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">LinguaAI</Link>
      </div>
      <div className={`navbar-menu ${isOpen ? 'is-active' : ''}`}>
        <Link to="/">Home</Link>
        <Link to="/summarize">Summarize Text</Link>
        <Link to="/analyze-sentiment">Analyze Sentiment</Link>
      </div>
      <div className="navbar-burger" onClick={() => setIsOpen(!isOpen)}>
        <span></span>
        <span></span>
        <span></span>
      </div>
    </nav>
  );
}

export default Navbar;