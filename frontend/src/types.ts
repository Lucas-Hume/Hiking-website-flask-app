export interface Trail {
  id: number;
  name: string;
  lat: number;
  lon: number;
  location: string;
  date: string;
  difficulty: "Easy" | "Moderate" | "Hard";
  distance_km: number;
  image_url: string;
  elevation: number;
  status: "upcoming" | "completed";
  weather?: {
    temperature: number | null;
    description: string;
  };
}