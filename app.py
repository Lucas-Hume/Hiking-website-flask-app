from flask import Flask, render_template
from services.weather import get_weather
from services.trails_service import get_upcoming_trails

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/upcoming_trails")
def upcoming():
    trails = get_upcoming_trails()

    for trail in trails:
        weather_info = get_weather(
        lat=trail["lat"],
        lon=trail["lon"]
        )
    return render_template("upcoming_trails.html", trails=trails)

@app.route("/completed_trails")
def completed():
    return render_template("completed_trails.html")

if __name__ == "__main__":
    app.run(debug=True)
