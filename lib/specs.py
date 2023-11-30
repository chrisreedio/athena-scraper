import requests
import json
import os
from termcolor import colored

baseUrl = "https://docs.athenahealth.com/v1/api/swagger/exploreDocs?urlAlias=/api-ref/"
output_dir = 'output/'

def fetchSpec(endpoint, category=None):
	"""
	Fetches a specification from the given endpoint and saves it as a JSON file.

	Args:
		endpoint (str): The endpoint URL to fetch the specification from.
		category (str, optional): The category of the specification. Defaults to None.

	Returns:
		None
	"""
	# Rest of the code...
def fetchSpec(endpoint, category=None):
	# Construct the full URL
	url = f"{baseUrl}{endpoint}"
	outputPath = os.path.join(output_dir, category or '')
	filename = endpoint + '.json'
	fullOutputPath = os.path.join(outputPath, filename)

	# Check if the file already exists
	if os.path.exists(fullOutputPath):
		print(colored('✓', 'yellow'))
		return

	# Make the HTTP request
	try:
		response = requests.get(url)
		response.raise_for_status()  # This will raise an error for HTTP errors

		# Parse and Format the JSON response
		jsonResponse = response.json()
		formattedJson = json.dumps(jsonResponse, indent=4)

		# Save the content to a file		
		if not os.path.exists(outputPath):
			os.makedirs(outputPath)

		with open(fullOutputPath, 'w') as file:
			file.write(formattedJson)

		print(colored('✓', 'green'))

	except requests.exceptions.HTTPError as err:
		print(colored(f"HTTP Error: {err}", 'red'))
	except requests.exceptions.RequestException as e:
		print(colored(f"Error: {e}", 'red'))