# app.py
from flask import Flask
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello from backend!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
