import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const MapComponent = () => {
  const [geoData, setGeoData] = useState(null);

  // Load ZIP code GeoJSON
  useEffect(() => {
    fetch("/htown-zipcodes.geojson") // Ensure this file is inside the public/ folder
      .then((response) => response.json())
      .then((data) => {
        setGeoData(data);
      })
      .catch((error) => console.error("Error loading GeoJSON:", error));
  }, []);

  // Style function to adjust stroke width
  const geoJsonStyle = (feature) => {
    return {
      weight: 1, // Set the stroke width here (1 is thinner)
      color: "blue", // Stroke color
      opacity: 1, // Opacity of the border
      fillColor: "lightblue", // Fill color for the polygons
      fillOpacity: 0.5, // Fill opacity
    };
  };

  // Handle GeoJSON features (add popups, etc.)
  const onEachFeature = (feature, layer) => {
    if (feature.properties && feature.properties.ZIPCODE) {
      layer.bindPopup(`<strong>ZIP Code:</strong> ${feature.properties.ZIPCODE}`);
    }
  };

  if (!geoData) {
    return <p>Loading map...</p>;
  }

  return (
    <MapContainer
      center={[29.7604, -95.3698]} // Houston's latitude and longitude
      zoom={10}
      style={{ height: "100vh", width: "100%" }} // Full height and width
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; OpenStreetMap contributors'
      />
      <GeoJSON
        data={geoData}
        onEachFeature={onEachFeature}
        style={geoJsonStyle} // Apply the style to the GeoJSON
      />
    </MapContainer>
  );
};

export default MapComponent;
