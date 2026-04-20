from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# Dummy weather data
weather_data = [
    {"status": "☀️ Sunny", "temp": "30°C"},
    {"status": "🌧️ Rainy", "temp": "20°C"},
    {"status": "⛅ Cloudy", "temp": "29°C"},
    {"status": "🌩️ Stormy", "temp": "25°C"},
]

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        # Validation
        if not city or not city.strip():
            error = "⚠️ Please enter a valid city name"
        elif not city.replace(" ", "").isalpha():
            error = "⚠️ City name should contain only letters"
        else:
            city = city.strip().title()
            selected = random.choice(weather_data)

            weather = {
                "city": city,
                "status": selected["status"],
                "temp": selected["temp"]
            }

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    # SAFE: no debug=True hardcoded
    debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(debug=debug_mode)
#updation