from flask import Flask, render_template, jsonify
import math
import time
import os

app = Flask(__name__)

PLANETS = {
    "Mercury": {"radius": 60, "speed": 4.15, "size": 5, "color": "gray"},
    "Venus": {"radius": 90, "speed": 1.62, "size": 8, "color": "orange"},
    "Earth": {"radius": 130, "speed": 1.0, "size": 9, "color": "blue"},
    "Mars": {"radius": 170, "speed": 0.53, "size": 7, "color": "red"},
    "Jupiter": {"radius": 220, "speed": 0.08, "size": 14, "color": "brown"},
}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/planets")
def planets():
    t = time.time()

    data = []

    for name, p in PLANETS.items():
        angle = t * p["speed"]

        x = 400 + p["radius"] * math.cos(angle)
        y = 300 + p["radius"] * math.sin(angle)

        data.append({
            "name": name,
            "x": x,
            "y": y,
            "size": p["size"],
            "color": p["color"]
        })

    return jsonify(data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)