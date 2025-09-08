from flask import Flask, request, Response
import datetime
import io
from PIL import Image

app = Flask(__name__)

@app.route('/track')
def track():
    # Log open event
    user_ip = request.remote_addr
    timestamp = datetime.datetime.now()
    with open("open_logs.txt", "a") as f:
        f.write(f"Email opened at {timestamp} from IP {user_ip}\n")

    # Create 1x1 white pixel dynamically
    img = Image.new("RGB", (1, 1), (255, 255, 255))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)

    return Response(buf, mimetype="image/jpeg")

@app.route('/')
def home():
    return "Email Tracker is running!"

if __name__ == '__main__':
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

