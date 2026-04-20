from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        # Input validation
        if city and city.strip():
            city = city.strip()
            weather = f"Weather in {city}: 🌤️ 30°C, Clear Sky"
        else:
            weather = "⚠️ Please enter a valid city name"

    return render_template("index.html", weather=weather)


if __name__ == "__main__":
    # Secure debug handling (no hardcoded debug=True)
    debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(debug=debug_mode)