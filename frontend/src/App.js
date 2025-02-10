import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get("https://eventscraper.onrender.com/events")
      .then(response => setEvents(response.data.events))
      .catch(error => console.error("Error fetching events:", error));
  }, []);

  return (
    <div style={{ textAlign: "center" }}>
      <h1>Sydney Events</h1>
      <div>
        {events.map((event, index) => (
          <div key={index} style={{ border: "1px solid #ccc", padding: "10px", margin: "10px", borderRadius: "8px" }}>
            <h2>{event.title}</h2>
            <p>Date: {event.date}</p>
            <a href={event.link} target="_blank" rel="noopener noreferrer">
              <button>GET TICKETS</button>
            </a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
