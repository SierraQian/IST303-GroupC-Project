from flask import Blueprint, render_template
from fredapi import Fred
from datetime import datetime

fred = Blueprint('fred', __name__)

# Initialize the FRED API client
api_key = '8bf74e8cf0c1a4bfcde0f5db0436df43'  # Replace with your actual FRED API key
fred_client = Fred(api_key=api_key)

# Define the list of indicator IDs (replace with any indicators)
indicator_ids = ['GDPC1', 'CPIAUCSL', 'UNRATE', 'PAYEMS', 'A191RL1Q225SBEA',
				 'MORTGAGE30US', 'PSAVERT', 'FEDFUNDS', 'SP500', 'VIXCLS']

@fred.route('/profile')
def profile():
	try:
		# Download the indicators' data
		indicators_data = fred_client.get_series(indicator_ids)

		# Format the data for display
		economic_calendar = []
		for indicator_id in indicator_ids:
			series = indicators_data[indicator_id]
			last_value = series.iloc[-1]
			next_publish_date = fred_client.get_series_info(indicator_id)['next_release_date']
			next_publish_date = datetime.strptime(next_publish_date, '%Y-%m-%d').strftime('%b %d, %Y')
			economic_calendar.append({
				'indicator_id': indicator_id,
				'previous_value': last_value,
				'next_publish_date': next_publish_date
			})

		return render_template('profile.html', economic_calendar=economic_calendar)

	except Exception as e:
		# Handle any exceptions that might occur during data retrieval or rendering
		error_message = f"An error occurred: {str(e)}"
		return render_template('error.html', error_message=error_message)
