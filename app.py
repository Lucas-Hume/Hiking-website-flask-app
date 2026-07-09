from flask import Flask, render_template,jsonify
from services.weather import get_weather
from services.trails_service import get_upcoming_trails, get_completed_trails
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/api/upcoming_trails")
def upcoming():
    trails = get_upcoming_trails()

    for trail in trails:
        weather_info = get_weather(
        lat=trail["lat"],
        lon=trail["lon"]
        )
    return jsonify(trails)

@app.route("/api/completed_trails")
def completed():
    trails=get_completed_trails()
    return jsonify(trails)

if __name__ == "__main__":
    app.run(debug=True)
