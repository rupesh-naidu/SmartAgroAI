import os
import sys

from flask import Flask, send_from_directory
from flask_cors import CORS

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(BASE_DIR)

from api.routes import register_routes

# ✅ Create Flask app
app = Flask(__name__, static_folder="../frontend")

CORS(app)

# ✅ Register API routes
register_routes(app)

# ✅ Serve frontend
@app.route("/")
def serve_frontend():
    return send_from_directory("../frontend", "index.html")

# ✅ Serve static files (JS, CSS, etc.)
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("../frontend", path)


if __name__ == "__main__":
    app.run(debug=True)