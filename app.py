from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        if city and city.strip():
            # Updated dummy weather
            weather = f"Weather in {city}: 🌤️ 37°C, Clear Sky"
        else:
            weather = "⚠️ Please enter a valid city name"

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)