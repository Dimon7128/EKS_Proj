from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from dotenv import load_dotenv
import requests
import json
import logging
from datetime import datetime
import os

load_dotenv()
app = Flask(__name__)

bg_color = os.getenv('BG_COLOR', '#FFFFFF')  # Default to white if not set
api_key = os.getenv('KEY_API')
history_dir = 'search_history'
os.makedirs(history_dir, exist_ok=True)  # Ensure the directory exists

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def get_input():
    json_data = {}
    if request.method == 'POST':
        user_input = request.form['user_input']
        url = (
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/"
            f"rest/services/timeline/{user_input}/next7days?unitGroup=metric&"
            f"key={api_key}&include=days&lang=en&iconSet=icons1"
        )
        logging.debug(f"Request URL: {url}")
        try:
            response = requests.get(url, timeout=10)
            logging.debug(f"Response Status Code: {response.status_code}")
            logging.debug(f"Response Content: {response.content}")
            if response.status_code == 200:
                json_data = response.json()
                save_search_to_history(user_input, json_data)
            else:
                logging.error(f"Error retrieving data. Status code: {response.status_code}")
                return redirect(url_for('error_page'))
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {e}")
            return redirect(url_for('error_page'))
    return render_template('input_form.html', api_data=json_data, bg_color=bg_color)

@app.route('/history')
def show_history():
    files = os.listdir(history_dir)
    files = [f for f in files if os.path.isfile(os.path.join(history_dir, f))]
    files.sort(reverse=True)  # Sort files by date
    return render_template('history.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(history_dir, filename, as_attachment=True)

@app.route('/error', methods=['GET'])
def error_page():
    return render_template('error.html')

def save_search_to_history(city, data):
    history_data = {
        'city': city,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        #'data': data  # This is the actual data received from the API
    }
    filename = f"{datetime.now().strftime('%Y-%m-%d')}_{city}.json"
    file_path = os.path.join(history_dir, filename)
    with open(file_path, 'a') as f:
        json.dump(history_data, f, indent=4)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
