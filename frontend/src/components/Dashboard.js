import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function Dashboard() {
  const { token, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = async () => {
    await axios.post("http://127.0.0.1:8000/api/logout/", {}, {
      headers: { Authorization: `Token ${token}` }
    });
    logout();
    navigate("/");
  };

  return (
    <div>
      <h2>Welcome to Dashboard</h2>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Dashboard;
