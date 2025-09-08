from flask import Flask, request, Response, redirect
import datetime
import io
from PIL import Image
import os

app = Flask(__name__)

# ----------------------------
# Utility function to get client IP
# ----------------------------
def get_client_ip():
    """Fetch the real client IP even if behind proxies."""
    if "X-Forwarded-For" in request.headers:
        # Can contain multiple IPs if there are multiple proxies
        ip = request.headers["X-Forwarded-For"].split(",")[0].strip()
    else:
        ip = request.remote_addr
    return ip

# ----------------------------
# Endpoint to track email opens
# ----------------------------
@app.route('/track')
def track():
    user_ip = get_client_ip()
    email_id = request.args.get("id", "unknown")   # ?id=user001
    timestamp = datetime.datetime.now()

    # Log to console
    print(f"[OPENED] Email ID={email_id}, IP={user_ip}, Time={timestamp}")

    # Create 1x1 white pixel dynamically
    img = Image.new("RGB", (1, 1), (255, 255, 255))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)

    return Response(buf, mimetype="image/jpeg")

# ----------------------------
# Endpoint to track link clicks
# ----------------------------
@app.route('/click')
def click():
    user_ip = get_client_ip()
    email_id = request.args.get("id", "unknown")   # ?id=user001
    timestamp = datetime.datetime.now()

    # Log click to console
    print(f"[CLICK] Email ID={email_id}, IP={user_ip}, Time={timestamp}")

    # Redirect to actual destination link
    destination_url = "https://example.com"  # Replace with your real link
    return redirect(destination_url)

# ----------------------------
# Health check
# ----------------------------
@app.route('/')
def home():
    return "✅ Email Tracker is running!"

# ----------------------------
# Run Flask app
# ----------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
