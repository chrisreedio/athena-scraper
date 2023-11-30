import requests
from bs4 import BeautifulSoup

# The URL of the page with the sidebar
url = 'https://docs.athenahealth.com/api/docs/appointments'

# Step 1: Fetch the webpage
response = requests.get(url)
response.raise_for_status()  # will raise an exception for HTTP errors

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find sidebar links
# You need to identify the correct class or id for the sidebar
sidebar_links = soup.select('.nav-links__list__level-2 a[href*="/api/api-ref/"]')

print('Sidebar Links:')
print(sidebar_links)

# Step 4: Filter and Format Links
endpoints = []
for link in sidebar_links:
    href = link.get('href')
    # if href and href.endswith('appointment'):  # Modify condition as needed
    endpoints.append(href)

# Now `endpoints` contains all the required links
print(endpoints)
