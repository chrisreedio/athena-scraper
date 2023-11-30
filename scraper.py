import os
import requests

output_dir = 'specs/'

def download_json_files(base_path, endpoints):
    global output_dir
    # Ensure the base path ends with a '/'
    if not base_path.endswith('/'):
        base_path += '/'

    for endpoint in endpoints:
        # Construct the full URL
        url = f"{base_path}{endpoint}"

        # Make the HTTP request
        try:
            response = requests.get(url)
            response.raise_for_status()  # This will raise an error for HTTP errors

            # Extract the filename from the endpoint
            filename = endpoint.split('/')[-1] + '.json'

            # Save the content to a file
            with open(output_dir + filename, 'w') as file:
                file.write(response.text)

            print(f"Downloaded '{filename}' successfully.")

        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Example usage
base_path = "https://docs.athenahealth.com/v1/api/swagger/exploreDocs?urlAlias=/api-ref/"
endpoints = ['appointment']

download_json_files(base_path, endpoints)
