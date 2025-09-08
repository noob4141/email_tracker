from flask import Flask, request, Response, redirect
import datetime
import io
from PIL import Image

app = Flask(__name__)

# ----------------------------
# Endpoint to track email opens
# ----------------------------
@app.route('/track')
def track():
    # Capture details
    user_ip = request.remote_addr
    email_id = request.args.get("id", "unknown")   # ?id=user001
    timestamp = datetime.datetime.now()

    # Log to Railway console
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
    user_ip = request.remote_addr
    email_id = request.args.get("id", "unknown")   # ?id=user001
    timestamp = datetime.datetime.now()

    # Log click to console
    print(f"[CLICK] Email ID={email_id}, IP={user_ip}, Time={timestamp}")

    # Redirect to actual destination link
    destination_url = "https://example.com"  # Change this to your real link
    return redirect(destination_url)


# ----------------------------
# Health check
# ----------------------------
@app.route('/')
def home():
    return "✅ Email Tracker is running on Railway!"


if __name__ == '__main__':
    # Railway uses port from env, fallback to 8080
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
