from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        if city and city.strip():
            city = city.strip().title()

            # Random weather simulation
            temp = random.randint(25, 40)
            conditions = ["Sunny ☀️", "Cloudy ☁️", "Rainy 🌧️", "Windy 🌬️"]
            condition = random.choice(conditions)

            weather = f"Weather in {city}: {condition}, {temp}°C"
        else:
            weather = "⚠️ Please enter a valid city name"

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)