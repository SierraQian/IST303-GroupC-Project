from fredapi import Fred
from datetime import datetime

# Initialize the FRED API client
fred = Fred(api_key='YOUR_FRED_API_KEY')

# Define the list of indicator IDs (replace with any indicators)
indicator_ids = ['GDPC1', 'CPIAUCSL', 'UNRATE', 'PAYEMS', 'A191RL1Q225SBEA',
				 'MORTGAGE30US', 'PSAVERT', 'FEDFUNDS', 'SP500', 'VIXCLS']

# Download the indicators' data
indicators_data = fred.get_series(indicator_ids)

# Format the data for display
economic_calendar = []
for indicator_id in indicator_ids:
	series = indicators_data[indicator_id]
	last_value = series.iloc[-1]
	next_publish_date = fred.get_series_info(indicator_id)['next_release_date']
	next_publish_date = datetime.strptime(next_publish_date, '%Y-%m-%d').strftime('%b %d, %Y')
	economic_calendar.append({
		'indicator_id': indicator_id,
		'previous_value': last_value,
		'next_publish_date': next_publish_date
	})
