""" import os
import sys

from flask import Flask
from flask_cors import CORS


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(BASE_DIR)


from routes import register_routes


app = Flask(__name__)

CORS(app)


register_routes(app)


if __name__ == "__main__":
    app.run(debug=True) """


import os
import sys

from flask import Flask, send_from_directory
from flask_cors import CORS

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(BASE_DIR)

from routes import register_routes

# 👇 Tell Flask where frontend is
app = Flask(__name__, static_folder="../frontend")

CORS(app)

register_routes(app)

# 👇 Serve frontend (index.html)
@app.route("/")
def serve_frontend():
    return send_from_directory("../frontend", "index.html")

# 👇 (Optional) serve other static files if needed
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("../frontend", path)

if __name__ == "__main__":
    app.run()