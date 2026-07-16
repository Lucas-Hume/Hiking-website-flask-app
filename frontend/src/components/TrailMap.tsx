import { useEffect, useRef } from "react";
import type { Trail } from "../types";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// Fix Leaflet's default marker icon paths, which break in Vite
import markerIconUrl from "leaflet/dist/images/marker-icon.png";
import markerIcon2xUrl from "leaflet/dist/images/marker-icon-2x.png";
import markerShadowUrl from "leaflet/dist/images/marker-shadow.png";

const defaultIcon = L.icon({
  iconUrl: markerIconUrl,
  iconRetinaUrl: markerIcon2xUrl,
  shadowUrl: markerShadowUrl,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

interface TrailMapProps {
  trails: Trail[];
}

export default function TrailMap({ trails }: TrailMapProps) {
  const mapRef = useRef<HTMLDivElement>(null);
  const mapInstanceRef = useRef<L.Map | null>(null);

  useEffect(() => {
    // Don't initialise if the div isn't ready or map already exists
    if (!mapRef.current || mapInstanceRef.current) return;

    // Create the map centred on Australia
    const map = L.map(mapRef.current).setView([-33.635, 150.284], 10);
    mapInstanceRef.current = map;

    // Load OpenStreetMap tiles (free, no API key needed)
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    // Add a marker for each trail
    trails.forEach((trail) => {
      L.marker([trail.lat, trail.lon], { icon: defaultIcon })
        .addTo(map)
        .bindPopup(
          `<strong>${trail.name}</strong><br/>
            ${trail.distance_km} km in length &nbsp;|&nbsp;  ${trail.elevation} m in elevation<br/>
            ${trail.difficulty} &nbsp;|&nbsp;  ${trail.date}`
        );
    });

    // destroy the map when the component unmounts
    return () => {
      map.remove();
      mapInstanceRef.current = null;
    };
  }, [trails]);

  return (
    <div
      ref={mapRef}
      style={{ height: "400px", width: "100%", borderRadius: "8px" }}
    />
  );
}