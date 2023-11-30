import requests
import json

baseUrl = "https://docs.athenahealth.com/v1/api/swagger/exploreDocs?urlAlias=/api-ref/"
output_dir = 'specs/'

def fetchSpec(endpoint):
	# Construct the full URL
	url = f"{baseUrl}{endpoint}"

	# Make the HTTP request
	try:
		response = requests.get(url)
		response.raise_for_status()  # This will raise an error for HTTP errors

		# Extract the filename from the endpoint
		filename = endpoint.split('/')[-1] + '.json'

		# Parse and Format the JSON response
		jsonResponse = response.json()
		formattedJson = json.dumps(jsonResponse, indent=4)

		# Save the content to a file
		with open(output_dir + filename, 'w') as file:
			file.write(formattedJson)

		print(f"Downloaded '{filename}' successfully.")

	except requests.exceptions.HTTPError as err:
		print(f"HTTP Error: {err}")
	except requests.exceptions.RequestException as e:
		print(f"Error: {e}")