
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "logs/raw_logs.txt"

@app.route("/")
def home():
    return "IoT Device Login Portal"

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")
    ip = request.remote_addr
    time = datetime.now()

    log_entry = f"{time} | IP: {ip} | USERNAME: {username} | PASSWORD: {password}\n"

    with open(LOG_FILE, "a") as file:
        file.write(log_entry)

    return "Login Failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
