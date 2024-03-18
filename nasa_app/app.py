#API_KEY_NASA: Nb6SJKGykZgc7aLyKCI4IptBrgxo53SzVXpbUYYr

from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

api_url = "https://api.nasa.gov/planetary/apod"
api_key = "Nb6SJKGykZgc7aLyKCI4IptBrgxo53SzVXpbUYYr"

app.route('/')

def index():
    params = {
        'api_key': api_key
    }

    response = requests.get(api_url,params=params)

    if response.status_code == 200:
        data = response.json()

        return render_template('index.html',data=data)
    else:
        return f"Error {response.status_code}"
    
    if __name__ == '_main_'