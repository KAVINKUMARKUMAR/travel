import React from "react";
import "./RegisterPage.css";
import { Link } from "react-router-dom";
import travelImage from '../assets/travel-vision-board.jpeg';
function RegisterPage() {
  return (
    <div className="register-wrapper">
      <div className="register-card">
        <div className="register-left">
          <h2>Create Your Account</h2>
          <p>Sign up to explore dream destinations and adventures!</p>

          <form className="register-form">
            <label>Username</label>
            <input type="text" placeholder="kavin" />

            <label>Email</label>
            <input type="email" placeholder="kavin@mail.com" />

            <label>Password</label>
            <input type="password" placeholder="Enter password" />

            <label>Confirm Password</label>
            <input type="password" placeholder="Confirm password" />

            <div className="checkbox-group">
              <input type="checkbox" id="terms" />
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
