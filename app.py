from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is my first web page using Python Flask."

if __name__ == "__main__":
    app.run(debug=True)