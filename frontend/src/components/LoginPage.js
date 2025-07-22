import React from "react";
import "./RegisterPage.css";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import travelImage1 from "../assets/2.jpeg";

function LoginPage() {
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    const username = e.target[0].value;
    const password = e.target[1].value;

    try {
      const res = await axios.post("http://127.0.0.1:8000/api/auth/login/", {
        username,
        password,
      });

      const token = res.data.token;
      localStorage.setItem("token", token); // ✅ store token for auth
      alert("Login successful");
      navigate("/"); // Go to home/dashboard
    } catch (err) {
  if (err.response && err.response.data) {
    alert(err.response.data.error || JSON.stringify(err.response.data));
  } else {
    alert("Something went wrong. Please try again later.");
  }
}
  };

  return (
    <div className="register-wrapper">
      <div className="register-card">
        <div className="register-left">
          <h2>Welcome Back</h2>
          <p>Login to continue your travel journey!</p>

          <form className="register-form" onSubmit={handleLogin}>
            <label>Username</label>
            <input type="text" placeholder="kavin" required />

            <label>Password</label>
            <input type="password" placeholder="Enter password" required />

            <div className="checkbox-group">
              <input type="checkbox" id="terms-login" />
              <label htmlFor="terms-login">
                I agree to the <a href="#">Terms & Conditions</a>
              </label>
            </div>

            <button type="submit">Login</button>

            <p className="form-link">
              Don't have an account? <Link to="/register">Sign up</Link>
            </p>
          </form>
        </div>

        <div className="register-right">
          <img src={travelImage1} alt="Login Illustration" />
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
