from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user
from . import db
import requests
import os

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():
	fred_data = dashboard()
	return render_template('index.html', fred_data=fred_data)

def get_fred_data(indicator):
	fred_api_key = os.getenv('FRED_API_KEY', '8bf74e8cf0c1a4bfcde0f5db0436df43') # Create an environment variable after requesting your own FRED API key
	url = f"https://api.stlouisfed.org/fred/series/observations?series_id={indicator}&api_key={fred_api_key}&file_type=json"
	response = requests.get(url)
	data = response.json()
	latest_data_point = data['observations'][-1]['value']
	return latest_data_point

def dashboard():
	indicator_ids = ['GDPC1', 'CPIAUCSL', 'UNRATE', 'PAYEMS', 'A191RL1Q225SBEA', 'MORTGAGE30US', 'PSAVERT', 'FEDFUNDS', 'SP500', 'VIXCLS']
	fred_data = {indicator: get_fred_data(indicator) for indicator in indicator_ids}
	return fred_data

@main.route('/profile')
@login_required
def profile():
	fred_data = dashboard()
	return render_template('profile.html', name=current_user.name, fred_data=fred_data)
