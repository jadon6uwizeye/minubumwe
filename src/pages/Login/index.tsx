import React, { useState, ChangeEvent, FormEvent } from 'react';
import './Login.css'; // Import the CSS file for styling
import { Link, useHistory } from 'react-router-dom';
import axios from 'axios';

interface FormData {
  username: string;
  password: string;
}

function Login() {
  const [formData, setFormData] = useState<FormData>({
    username: '',
    password: '',
  });
  
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const history = useHistory();

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/accounts/login/',
        formData
      );

      if (response.status === 200) {
        // Successful login, set success message and redirect to landing page
        setSuccessMessage('Login successful.');
        setErrorMessage(null); // Clear any previous error message
        history.push('/home');
      } else {
        // Handle login error here, e.g., display an error message
        setErrorMessage('Login failed. Please check your credentials.');
        setSuccessMessage(null); // Clear any previous success message
      }
    } catch (error) {
      // Handle login error here, e.g., display an error message
      setErrorMessage('An error occurred during login.');
      setSuccessMessage(null); // Clear any previous success message
      console.error('Login error:', error);
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-container">
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-container">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      {successMessage && <p className="success-message">{successMessage}</p>}
      <p>
        Don't have an account? <Link to="/register">Sign up</Link>
      </p>
    </div>
  );
}

export default Login;
