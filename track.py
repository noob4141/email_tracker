from flask import Flask, request, send_file
import datetime

app = Flask(__name__)

@app.route('/track')
def track():
    email_id = request.args.get("id", "unknown")
    user_ip = request.remote_addr
    timestamp = datetime.datetime.now()

    log_line = f"Email {email_id} opened at {timestamp} from IP {user_ip}\n"
    print(log_line)  # live logs in Railway
    with open("open_logs.txt", "a") as f:
        f.write(log_line)

    return send_file("pixel.jpg", mimetype="image/jpeg")

@app.route('/')
def home():
    return "✅ Email tracker is running!"
