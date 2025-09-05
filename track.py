from flask import Flask, request, send_file
import datetime

app = Flask(__name__)

@app.route('/track')
def track():
    user_ip = request.remote_addr
    timestamp = datetime.datetime.now()
    with open("open_logs.txt", "a") as f:
        f.write(f"Email opened at {timestamp} from IP {user_ip}\n")

    # return 1x1 JPG instead of PNG
    return send_file("pixel.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
