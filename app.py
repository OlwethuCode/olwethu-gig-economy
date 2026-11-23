from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", page="home")


@app.route("/research")
def research():
    return render_template("research.html", page="research")


@app.route("/career")
def career():
    return render_template("career.html", page="career")


if __name__ == "__main__":
    app.run(debug=True)
