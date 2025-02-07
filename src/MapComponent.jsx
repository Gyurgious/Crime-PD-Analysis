import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, GeoJSON, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const MapComponent = () => {
  const [geoData, setGeoData] = useState(null);

  // Load ZIP code GeoJSON
  useEffect(() => {
    fetch("/houston-tx_.geojson") // Ensure this file is inside the public/ folder
      .then((response) => response.json())
      .then((data) => {
        setGeoData(data);
      })
      .catch((error) => console.error("Error loading GeoJSON:", error));
  }, []);

  return (
    <MapContainer style={{ height: "100vh", width: "100%" }} zoom={10}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />

      {/* Apply Auto-Zoom to ZIP Code Boundaries */}
      {geoData && <AutoZoom geoData={geoData} />}
      {geoData && (
        <GeoJSON
          data={geoData}
          style={() => ({
            color: "blue",
            weight: 2,
            fillColor: "lightblue",
            fillOpacity: 0.3,
          })}
          onEachFeature={(feature, layer) => {
            const zipCode = feature.properties.ZIPCode || "Unknown";
            layer.bindPopup(`<b>ZIP Code:</b> ${zipCode}`);
          }}
        />
      )}
    </MapContainer>
  );
};

// ** Auto-zoom to Fit ZIP Code Boundaries **
const AutoZoom = ({ geoData }) => {
  const map = useMap();

  useEffect(() => {
    if (!geoData || !geoData.features || geoData.features.length === 0) return;

    // Collect all polygon coordinates
    const bounds = [];
    geoData.features.forEach((feature) => {
      if (feature.geometry.type === "Polygon") {
        feature.geometry.coordinates[0].forEach((coord) => {
          bounds.push([coord[1], coord[0]]); // Leaflet expects [lat, lng]
        });
      } else if (feature.geometry.type === "MultiPolygon") {
        feature.geometry.coordinates.forEach((polygon) => {
          polygon[0].forEach((coord) => {
            bounds.push([coord[1], coord[0]]);
          });
        });
      }
    });

    // Apply fitBounds if boundaries exist
    if (bounds.length > 0) {
      map.fitBounds(bounds);
    }
  }, [geoData, map]);

  return null;
};

export default MapComponent;
