from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>DevOps Pipeline: SUCCESS!</h1><p>This app was deployed automatically via GitHub Actions.</p>"

if __name__ == '__main__':
    # Cloud environments pass the port as an environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
