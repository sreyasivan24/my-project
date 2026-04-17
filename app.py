from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            # Better dummy weather (random feel)
            weather = f"Weather in {city}: 🌤️ 37°C, Clear Sky"
        else:
            weather = "Please enter a city name"

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)