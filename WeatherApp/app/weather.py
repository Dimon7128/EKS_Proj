import logging
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from dotenv import load_dotenv
import requests
import json
from datetime import datetime
import os

load_dotenv()
app = Flask(__name__)

bg_color = os.getenv('BG_COLOR', '#FFFFFF')
api_key = os.getenv('KEY_API')
history_dir = 'search_history'
os.makedirs(history_dir, exist_ok=True)

# Load version
with open('VERSION', 'r') as f:
    app_version = f.read().strip()

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logging.debug(f"API Key: {api_key}")
logging.debug(f"Background Color: {bg_color}")
logging.debug(f"App Version: {app_version}")

@app.route('/', methods=['GET', 'POST'])
def get_input():
    logging.debug("Entered get_input route")
    json_data = {}
    if request.method == 'POST':
        user_input = request.form['user_input']
        logging.debug(f"User input: {user_input}")
        url = (
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/"
            f"rest/services/timeline/{user_input}/next7days?unitGroup=metric&"
            f"key={api_key}&include=days&lang=en&iconSet=icons1"
        )
        logging.debug(f"Request URL: {url}")
        try:
            response = requests.get(url, timeout=10)
            logging.debug(f"Response Status Code: {response.status_code}")
            if response.status_code == 200:
                json_data = response.json()
                logging.debug(f"API Response: {json_data}")
                save_search_to_history(user_input, json_data)
            else:
                logging.error(f"Error retrieving data. Status code: {response.status_code}")
                logging.error(f"Response Content: {response.text}")
                return redirect(url_for('error_page'))
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {e}")
            return redirect(url_for('error_page'))
    return render_template('input_form.html', api_data=json_data, bg_color=bg_color, app_version=app_version)

@app.route('/history')
def show_history():
    logging.debug("Entered show_history route")
    files = os.listdir(history_dir)
    files = [f for f in files if os.path.isfile(os.path.join(history_dir, f))]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(history_dir, f)), reverse=True)
    return render_template('history.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    logging.debug(f"Downloading file: {filename}")
    return send_from_directory(history_dir, filename, as_attachment=True)

@app.route('/error', methods=['GET'])
def error_page():
    logging.debug("Entered error_page route")
    return render_template('error.html')

def save_search_to_history(city, data):
    logging.debug(f"Saving search to history for city: {city}")
    history_data = {
        'city': city,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    filename = f"{city}.json"
    file_path = os.path.join(history_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
        if isinstance(existing_data, list):
            existing_data.append(history_data)
        else:
            existing_data = [existing_data, history_data]
        existing_data.sort(key=lambda x: x['date'], reverse=True)
    else:
        existing_data = [history_data]
    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
