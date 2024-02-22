from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Endpoint to fetch user data
USER_API = 'https://reqres.in/api/users'

@app.route('/')
def index():
    # Fetch user data from the API
    response = requests.get(USER_API)
    if response.status_code == 200:
        users = response.json().get('data', [])
        return render_template('index.html', users=users)
    else:
        return "Failed to fetch user data", 500

if __name__ == '__main__':
    app.run(debug=True, port=int("3000"), host="0.0.0.0")
