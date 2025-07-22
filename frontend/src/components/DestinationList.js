import React, { useEffect, useState } from 'react';

function DestinationList() {
  const [destinations, setDestinations] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/destinations/')
      .then((response) => response.json())
      .then((data) => setDestinations(data));
  }, []);

  return (
    <div className="p-4 grid grid-cols-1 md:grid-cols-3 gap-4">
      {destinations.map((place) => (
        <div key={place.id} className="border p-4 rounded shadow bg-white">
          <h2 className="text-xl font-semibold">{place.name}</h2>
          <p className="text-gray-700">{place.description}</p>
          {place.image && (
            <img src={`http://127.0.0.1:8000${place.image}`} alt={place.name} className="mt-2 w-full h-40 object-cover" />
          )}
        </div>
      ))}
    </div>
  );
}

export default DestinationList;
