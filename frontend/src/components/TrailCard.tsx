import type { Trail } from "../types";

interface TrailCardProps {
  trail: Trail;
}

const difficultyColour: Record<Trail["difficulty"], string> = {
  Easy:     "bg-emerald-900 text-emerald-300",
  Moderate: "bg-amber-900 text-amber-300",
  Hard:     "bg-red-900 text-red-300",
};

export default function TrailCard({ trail }: TrailCardProps) {
  return (
    <div className="bg-stone-900 border border-stone-700 rounded-xl overflow-hidden hover:border-stone-500 transition-colors">
      {trail.image_url && (
      <img
        src={`/static/${trail.image_url}`}
        alt={trail.name}
        className="w-full h-40 object-cover"
      />
      )}

      <div className="p-4 space-y-3">

        <div className="flex items-start justify-between gap-2">
          <h2 className="text-lg font-semibold text-stone-100">{trail.name}</h2>
          <span className={`text-xs font-medium px-2 py-1 rounded-full shrink-0 ${difficultyColour[trail.difficulty]}`}>
            {trail.difficulty}
          </span>
        </div>

        <p className="text-stone-400 text-sm">{trail.location}</p>

        <div className="grid grid-cols-2 gap-2 text-sm text-stone-300">
          <span>{trail.distance_km} km</span>
          <span>{trail.elevation} m gain</span>
          <span>{trail.date}</span>
        </div>

        {trail.weather && (
          <div className="text-sm text-stone-400 border-t border-stone-700 pt-3">
            {trail.weather.temperature}°C — {trail.weather.description}
          </div>
        )}

      </div>
    </div>
  );
}