from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Cloud Computing Lab</h1><p>Version 1 - Deployed by Jenkins CI/CD</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)