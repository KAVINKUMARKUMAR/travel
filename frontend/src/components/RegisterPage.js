import React from "react";
import "./RegisterPage.css";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import travelImage from "../assets/travel-vision-board.jpeg";

function RegisterPage() {
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();

    const username = e.target[0].value;
    const email = e.target[1].value;
    const password = e.target[2].value;
    const confirmPassword = e.target[3].value;

    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    try {
      const res = await axios.post("http://127.0.0.1:8000/api/auth/register/", {
        username,
        email,
        password,
      });

      alert(res.data.message || "Registered successfully");
      navigate("/login"); // ✅ go to login page after register
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
          <h2>Create Your Account</h2>
          <p>Sign up to explore dream destinations and adventures!</p>

          <form className="register-form" onSubmit={handleRegister}>
            <label>Username</label>
            <input type="text" placeholder="kavin" required />

            <label>Email</label>
            <input type="email" placeholder="kavin@mail.com" required />

            <label>Password</label>
            <input type="password" placeholder="Enter password" required />

            <label>Confirm Password</label>
            <input type="password" placeholder="Confirm password" required />

            <div className="checkbox-group">
              <input type="checkbox" id="terms" required />
              <label htmlFor="terms">
                I agree to the <a href="#">Terms & Conditions</a>
              </label>
            </div>

            <button type="submit">Sign up</button>

            <p className="form-link">
              Already have an account? <Link to="/login">Login</Link>
            </p>
          </form>
        </div>
        <div className="register-right">
          <img src={travelImage} alt="Register Illustration" />
        </div>
      </div>
    </div>
  );
}

export default RegisterPage;
