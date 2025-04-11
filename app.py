from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Shah Final Test API Server"

@app.route("/host")
def host():
    import socket
    return f"Host: {socket.gethostname()}"

@app.route("/ip")
def ip():
    import requests
    return f"Public IP: {requests.get('https://api.ipify.org').text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
