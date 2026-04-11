import os
import sys
from flask import Flask
from flask_cors import CORS

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(BASE_DIR)

from api.routes import register_routes

# ✅ Create Flask app
app = Flask(__name__)

# ✅ Enable CORS (Allows Vercel frontend to fetch from Render backend)
CORS(app)

# ✅ Register API routes
register_routes(app)

# ✅ Health check route
@app.route("/")
def home():
    return {"message": "SmartAgroAI Backend Running 🚀"}

if __name__ == "__main__":
    app.run(debug=True)