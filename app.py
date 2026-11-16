
# web app

from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load DBS model
model = joblib.load("dbs.pkl")

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    return render_template("main.html")

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return render_template("dbs.html")

@app.route("/dbsResult",methods=["POST"])
def dbsResult():
    q = request.form.get("q", type=float)

    if q is None or q <= 0:
        return render_template("dbs.html",
                               error="Please enter a valid exchange rate.")

    x = pd.DataFrame({"SGD": [q]})
    r = model.predict(x)

    return render_template("dbsResult.html",
                           r=round(float(r[0][0]), 2))

if __name__ == "__main__":
    app.run(port=5001)
