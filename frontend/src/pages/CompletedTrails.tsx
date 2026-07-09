import { useState, useEffect } from "react";
import type { Trail } from "../types";
import TrailCard from "../components/TrailCard";
import TrailMap from "../components/TrailMap";

export default function CompletedTrails() {
  // 1. State first
  const [completedTrails, setCompletedTrails] = useState<Trail[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // 2. useEffect second
  useEffect(() => {
    async function fetchTrails() {
      try {
        const res = await fetch("/api/completed_trails");
        const data = await res.json();
        setCompletedTrails(data);
      } catch (err) {
        setError("Could not load trails. Is Flask running?");
      } finally {
        setLoading(false);
      }
    }

    fetchTrails();
  }, []);

  // 3. Loading/error checks third
  if (loading) return (
    <div className="min-h-screen flex items-center justify-center bg-stone-950">
      <p className="text-stone-400 text-lg animate-pulse">Loading completed trails...</p>
    </div>
  );

  if (error) return (
    <div className="min-h-screen flex items-center justify-center bg-stone-950">
      <p className="text-red-400 text-lg">{error}</p>
    </div>
  );

  // 4. Return last
  return (
    <div className="min-h-screen bg-stone-950 text-stone-100 px-6 py-10">
        <TrailMap trails={completedTrails} />
      <div className="max-w-5xl mx-auto">
        <h2 className="text-xl font-semibold mb-4 text-stone-200">Completed Trails</h2>
        {completedTrails.length === 0 ? (
          <p className="text-stone-500">No completed trails.</p>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {completedTrails.map((trail) => (
              <TrailCard key={trail.id} trail={trail} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}