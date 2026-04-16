from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")
        
        # Simple dummy weather (for now)
        weather = f"Weather in {city}: Sunny ☀️, 100°C"

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)