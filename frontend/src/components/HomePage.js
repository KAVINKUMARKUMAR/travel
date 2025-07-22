// HomePage.js
import React, { useEffect, useState } from "react";
import axios from "axios";
import "./HomePage.css";
import DestinationList from './DestinationList';

function HomePage() {
  const [destinations, setDestinations] = useState([]);
  const [search, setSearch] = useState("");
  const [date, setDate] = useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/destinations/")
      .then(res => setDestinations(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="home">
      <nav className="navbar">
        <div className="logo">Real <span>Adventures</span></div>
        <div className="nav-links">
          <a href="#">Destinations</a>
          <a href="#">Vacations</a>
          <a href="#">Travel Services</a>
          <button className="btn">Get Your Listing</button>
        </div>
      </nav>

      <header className="hero">
        <h1>Live is an Adventure, Live it!</h1>
        <p>Don't be boring when you don’t explore, start your adventure now!</p>

        <div className="search-box">
          <input type="text" placeholder="Destination" value={search} onChange={(e) => setSearch(e.target.value)} />
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
          <button className="btn">Explore Now</button>
        </div>
      </header>

      <section className="adventures">
        <h2>Choose Your Next Adventure</h2>
        <div className="tags">
          {["Bed & Breakfast", "Campground", "RV Parks", "Hotels & Resort", "Vacation Rental", "Youth Hostel"].map(tag => (
            <button key={tag} className="tag">{tag}</button>
          ))}
        </div>

        <div className="destinations-grid">
          {destinations.map(dest => (
            <div key={dest.id} className="destination-card">
              <img src={`http://127.0.0.1:8000${dest.image}`} alt={dest.name} />
              <h3>{dest.name}</h3>
              <p>{dest.description}</p>
            </div>
          ))}
        </div>
      </section>
      <DestinationList />
    </div>
    
  );
}

export default HomePage;
