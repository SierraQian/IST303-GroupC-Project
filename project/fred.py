import requests, os

def get_standard_data(indicator):
	fred_api_key = os.getenv('FRED_API_KEY', '8bf74e8cf0c1a4bfcde0f5db0436df43')
	url_series = f"https://api.stlouisfed.org/fred/series?series_id={indicator}&api_key={fred_api_key}&file_type=json" # Get an economic data series
	url_observations = f"https://api.stlouisfed.org/fred/series/observations?series_id={indicator}&api_key={fred_api_key}&file_type=json" # Get the observations or data values for an economic data series
	
	response_series = requests.get(url_series)
	data_series = response_series.json()
	
	try:
		series_title = data_series['seriess'][0]['title']
		series_notes = data_series['seriess'][0]['notes']
	except (KeyError, IndexError): # When the expected key is not found or when the list index is out of range, return N/A
		series_title = "N/A"
		series_notes = "N/A"
	
	response_observations = requests.get(url_observations)
	data_observations = response_observations.json()
	
	try:
		latest_data_point_value = data_observations['observations'][-1]['value']
		latest_data_point_date = data_observations['observations'][-1]['date']
	except (KeyError, IndexError): # When the expected key is not found or when the list index is out of range, return N/A
		latest_data_point_value = "N/A"
		latest_data_point_date = "N/A"
	
	try:
		previous_data_point_value = data_observations['observations'][-2]['value']
		previous_data_point_date = data_observations['observations'][-2]['date']
	except (KeyError, IndexError): # When the expected key is not found or when the list index is out of range, return N/A
		previous_data_point_value = "N/A"
		previous_data_point_date = "N/A"

	# # Leverage float_to_money()
	# 
	# try:
	# 	latest_data_point_value = float_to_money(data_observations['observations'][-1]['value'])
	# 	latest_data_point_date = data_observations['observations'][-1]['date']
	# except (KeyError, IndexError): 
	# 	latest_data_point_value = "N/A"
	# 	latest_data_point_date = "N/A"
	# 
	# try:
	# 	previous_data_point_value = float_to_money(data_observations['observations'][-2]['value'])
	# 	previous_data_point_date = data_observations['observations'][-2]['date']
	# except (KeyError, IndexError): 
	# 	previous_data_point_value = "N/A"
	# 	previous_data_point_date = "N/A"
	
	return series_title, latest_data_point_value, latest_data_point_date, previous_data_point_value, previous_data_point_date, series_notes

def get_standard_data_dashboard():
		indicator_ids = ['GDPC1', 'CPIAUCSL', 'UNRATE', 'PAYEMS', 'A191RL1Q225SBEA', 'MORTGAGE30US', 'PSAVERT', 'FEDFUNDS', 'SP500', 'VIXCLS']
		standard_data = {indicator: get_standard_data(indicator) for indicator in indicator_ids}
		return standard_data

def customized_dashboard(indicator_ids, standard_data):
	if not indicator_ids:
		return standard_data
	else:
		return {indicator: get_standard_data(indicator) for indicator in indicator_ids}
		
# # Convert Integers into a readable format (Money)
# 		
# def float_to_money(amount, currency_symbol="$"):
# 	try:
# 		amount = float(amount)
# 		return f"{currency_symbol}{amount:,.2f}"
# 	except ValueError:  # raised when trying to convert a string that doesn't represent a number
# 		return amount

