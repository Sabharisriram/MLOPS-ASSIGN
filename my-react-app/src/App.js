import React, { useState } from 'react';
import axios from 'axios';
import './styles.css'; // Import the CSS file

function App() {
  const [Age, setAge] = useState('');
  const [Sex, setSex] = useState('');
  const [Bmi, setBmi] = useState('');
  const [Smoker, setSmoker] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const handleInputChange = (e, setInputFunction) => {
    setInputFunction(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/', {
        age: Age,
        sex: Sex,
        bmi: Bmi,
        smoker: Smoker
      });
      setOutput(response.data.output);
      setError('');
    } catch (error) {
      console.error('Error:', error);
      setError('Error: Something went wrong. Please try again.');
      setOutput('');
    }
  };

  return (
    <div className="container">
      <h1>medical cost prediction</h1>
      <form onSubmit={handleSubmit} className="form">
        <div className="input-group">
          <label>Age:</label>
          <input type="text" value={Age} onChange={(e) => handleInputChange(e, setAge)} />
        </div>
        <div className="input-group">
          <label>Sex:</label>
          <input type="text" value={Sex} onChange={(e) => handleInputChange(e, setSex)} />
        </div>
        <div className="input-group">
          <label>Bmi:</label>
          <input type="text" value={Bmi} onChange={(e) => handleInputChange(e, setBmi)} />
        </div>
        <div className="input-group">
          <label>Smoker:</label>
          <input type="text" value={Smoker} onChange={(e) => handleInputChange(e, setSmoker)} />
        </div>
        <button type="submit" className="button">Submit</button>
      </form>
      {error && <div style={{ color: 'red', marginTop: '10px' }}>{error}</div>}
      {output && <div style={{ marginTop: '10px' }}>{output}</div>}
    </div>
  );
}

export default App;
