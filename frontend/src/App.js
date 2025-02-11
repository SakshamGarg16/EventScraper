import React, { useEffect, useState } from "react";
import axios from "axios";
import ParticleBackground from "./ParticleBackground";

const App = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios
      .get("https://eventscraper.onrender.com/events")
      .then((response) => setEvents(response.data.events))
      .catch((error) => console.error("Error fetching events:", error));
  }, []);

  return (
    <div className="relative min-h-screen flex flex-col items-center justify-center px-6 py-12">
      {/* Animated Particle Background */}
      <ParticleBackground />

      {/* Main Content */}
      <div className="relative z-10 text-white flex flex-col items-center">
        <div className="bg-black bg-opacity-60 backdrop-blur-md p-6 rounded-xl shadow-lg">
          <h1 className="text-4xl font-bold drop-shadow-lg mb-6">🎉 Sydney Events</h1>
        </div>

        {events.length === 0 ? (
          <div className="flex items-center justify-center h-96">
            <p className="text-white text-lg animate-pulse">Fetching events...</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 w-full max-w-6xl mt-6">
            {events.map((event, index) => (
              <div
                key={index}
                className="bg-white bg-opacity-20 backdrop-blur-lg p-6 rounded-xl shadow-xl transition-transform transform hover:-translate-y-2 hover:shadow-2xl"
              >
                <h2 className="text-xl font-semibold text-white">{event.title}</h2>
                <p className="text-gray-200 text-sm mt-2">📅 {event.date}</p>
                <a href={event.link} target="_blank" rel="noopener noreferrer">
                  <button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition duration-300">
                    🎟️ GET TICKETS
                  </button>
                </a>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
