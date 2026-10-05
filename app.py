import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from services.analytics_service import AnalyticsService

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin Resource Sharing if needed

# --- PAGES ---

@app.route("/")
def index():
    """Serves the main single-page application."""
    return render_template("index.html")

# --- API ENDPOINTS ---

@app.route("/api/v1/stats", methods=["GET"])
def get_stats():
    """Returns analytics and system status metrics."""
    data = AnalyticsService.get_dashboard_stats()
    return jsonify(data), 200

@app.route("/api/v1/settings", methods=["POST"])
def save_settings():
    """Receives and processes configuration updates (e.g. accent colors)."""
    payload = request.get_json() or {}
    response = AnalyticsService.update_settings(payload)
    return jsonify(response), 200

# --- HEALTH CHECK ---

@app.route("/health", methods=["GET"])
def health_check():
    """Simple status check endpoint."""
    return jsonify({"status": "healthy", "service": "dashboard-api"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
