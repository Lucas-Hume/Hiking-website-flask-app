# Hiking Trails Planner (Flask Web App)

A Flask-based web application that showcases upcoming and completed hiking trails, integrating live weather data and map embeds.

This project demonstrates backend fundamentals, API integration, templating, and basic frontend styling.

---

## Features

- Home page with navigation
- Upcoming hiking trails page
- Google Maps embeds for trail locations
- Live weather data using OpenWeather API
- JSON-based trail data storage
- Flask routing and Jinja templating
- Environment variable usage for API keys

---

## Tech Stack

- Python
- Flask
- HTML / CSS
- OpenWeather API
- Google Maps Embed
- GitHub

---

## Project Structure

project-root/
│
├── app.py
├── services/
│ ├── weather.py
│ ├── trails_service.py
│ └── trails.json
│
├── templates/
│ ├── homepage.html
│ ├── upcoming_trails.html
│ └── completed_trails.html
│
├── static/
│ └── style.css
│
└── README.md


---

## Setup Instructions

1. Clone the repository
2. Create a virtual environment (optional but recommended)
3. Install dependencies
4. Set your OpenWeather API key as an environment variable:

### Windows (PowerShell)

---

## Setup Instructions

1. Clone the repository
2. Create a virtual environment (optional but recommended)
3. Install dependencies
4. Set your OpenWeather API key as an environment variable:

### Windows (PowerShell)
setx OPENWEATHER_API_KEY "your_api_key_here"


5. Run the app:

setx OPENWEATHER_API_KEY "your_api_key_here"


python app.py

6. Open your browser at:
python app.py
http://127.0.0.1:5000


---

## What This Project Demonstrates

- Understanding of Flask app structure
- API consumption and error handling
- Passing data from backend to frontend
- Environment variable usage
- Incremental project development

---

## Planned Improvements

- Trail filtering and sorting
- Photo uploads for completed trails
- Deployment (Render / Railway)
- Improved UI styling

---

## Author

Lucas Hume
