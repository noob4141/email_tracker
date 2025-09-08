from flask import Flask, request, Response
import datetime
import io
from PIL import Image

app = Flask(__name__)

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

@app.route('/')
def home():
    return "✅ Email Tracker is running on Railway!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
