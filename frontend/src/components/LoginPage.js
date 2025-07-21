import React from "react";
import "./RegisterPage.css";
import { Link } from "react-router-dom";
import travelImage1 from '../assets/2.jpeg';
function LoginPage() {
  return (
    <div className="register-wrapper">
      <div className="register-card">
        <div className="register-left">
          <h2>Welcome Back</h2>
          <p>Login to continue your travel journey!</p>

          <form className="register-form">
            <label>Username</label>
            <input type="text" placeholder="kavin" />

            <label>Password</label>
            <input type="password" placeholder="Enter password" />

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
          <img
            src={travelImage1}
            alt="Login Illustration"
          />
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
