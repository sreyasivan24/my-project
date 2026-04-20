from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        # Input validation (important for security)
        if city and city.strip():
            city = city.strip()

            # Safe dummy weather output
            weather = f"Weather in {city}: 🌤️ 30°C, Clear Sky"
        else:
            weather = "⚠️ Please enter a valid city name"

    return render_template("index.html", weather=weather)


if __name__ == "__main__":
    app.run(debug=True)