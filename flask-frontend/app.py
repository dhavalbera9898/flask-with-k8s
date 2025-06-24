from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get("http://express-backend:3000/")
    return f"Hello from Flask! Backend says: {r.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
