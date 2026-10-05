import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from services.data_service import DataService

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    """Renders the dashboard UI."""
    return render_template("index.html")

@app.route("/api/v1/analytics", methods=["GET"])
def fetch_analytics():
    """
    API endpoint returning dynamically calculated analytics based on query parameters.
    Example: /api/v1/analytics?region=us-east&days=14&mode=turbo
    """
    region = request.args.get("region", "global")
    try:
        days = int(request.args.get("days", 7))
    except ValueError:
        days = 7
    mode = request.args.get("mode", "standard")

    data = DataService.get_filtered_data(region=region, days=days, performance_mode=mode)
    return jsonify(data), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
