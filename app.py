from flask import Flask, request, jsonify, redirect
from shortener import shorten_url, get_original_url

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "URL Shortener API",
        "status": "Running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/shorten", methods=["POST"])
def create_short_url():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    code = shorten_url(data["url"])

    return jsonify({
        "short_code": code,
        "short_url": request.host_url + code
    })


@app.route("/<code>")
def redirect_url(code):
    original_url = get_original_url(code)

    if original_url:
        return redirect(original_url)

    return jsonify({
        "error": "URL not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)