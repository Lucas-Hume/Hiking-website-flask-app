import os,requests, json




api_key = os.getenv("OPENWEATHER_API_KEY")
base_url= "https://api.openweathermap.org/data/2.5/weather"

def get_weather(lat=None, lon=None, units="metric"):
    params={
        "appid": api_key,
        "units": units
    }
    if lat and lon:
        params["lat"]= lat
        params["lon"]= lon
    else:
        return None
    try:
        response= requests.get(base_url, params=params,timeout=5)
        response.raise_for_status()
        data= response.json()

        return{
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    
    except Exception:
        return {
            "temperature": None,
            "descriptions": "Weather data unavailable"
        }



