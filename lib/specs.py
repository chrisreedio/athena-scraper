import requests
import json
import os
from termcolor import colored

baseUrl = "https://docs.athenahealth.com/v1/api/swagger/exploreDocs?urlAlias=/api-ref/"
output_dir = 'specs/'

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

		# Extract the filename from the endpoint
		# filename = endpoint.split('/')[-1] + '.json'
		

		# Parse and Format the JSON response
		jsonResponse = response.json()
		formattedJson = json.dumps(jsonResponse, indent=4)

		# Save the content to a file
		
		if not os.path.exists(outputPath):
			os.makedirs(outputPath)

		with open(fullOutputPath, 'w') as file:
			file.write(formattedJson)

		print(colored('✓', 'green'))
		# print(f"Downloaded '{filename}' successfully.")

	except requests.exceptions.HTTPError as err:
		print(colored(f"HTTP Error: {err}", 'red'))
	except requests.exceptions.RequestException as e:
		print(colored(f"Error: {e}", 'red'))