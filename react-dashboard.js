import React, { useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [topic, setTopic] = useState('');
  const [depth, setDepth] = useState('medium');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/research', {
        topic,
        depth
      }, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      });
      setResults(response.data);
    } catch (error) {
      console.error('Error conducting research:', error);
    }
    setLoading(false);
  };

  return (
    <div className="dashboard">
      <h1>OSINT Research Dashboard</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="Enter research topic"
          required
        />
        <select value={depth} onChange={(e) => setDepth(e.target.value)}>
          <option value="shallow">Shallow</option>
          <option value="medium">Medium</option>
          <option value="deep">Deep</option>
        </select>
        <button type="submit" disabled={loading}>
          {loading ? 'Researching...' : 'Conduct Research'}
        </button>
      </form>
      {results && (
        <div className="results">
          <h2>Research Results</h2>
          <h3>{results.topic}</h3>
          <ul>
            {results.findings.map((finding, index) => (
              <li key={index}>{finding}</li>
            ))}
          </ul>
          <h3>Sources</h3>
          <ul>
            {results.sources.map((source, index) => (
              <li key={index}>{source}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
