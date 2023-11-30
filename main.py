from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pprint import pprint

baseUrl = 'https://docs.athenahealth.com/api/docs/'

def fetchLinks(url, selector):
	# Setup Selenium with a headless browser (no GUI)
	options = Options()
	chromePath = '/snap/bin/chromium.chromedriver'
	options.add_argument("--headless")  # if you want the browser to be headless
	options.add_argument("--no-sandbox")
	options.add_argument("--disable-dev-shm-usage") #Replace with the path to your Chrome installation
	options.headless = True
	# Set up service with the path to the chromedriver
	service = Service(executable_path=chromePath)
	driver = webdriver.Chrome(service=service, options=options)

	# Open the page
	# driver.get('https://docs.athenahealth.com/api/docs/appointments')
	print('Fetching links from: ' + baseUrl + url)
	driver.get(baseUrl + url)

	# Wait for JavaScript to load
	driver.implicitly_wait(10)  # You can adjust the wait time as needed

	# Now you can find elements just like in BeautifulSoup
	# links = driver.find_elements(By.CSS_SELECTOR, '.nav-links__list__level-2 a[href*="/api/api-ref/"]')
	links = driver.find_elements(By.CSS_SELECTOR, selector)

	endpoints = [link.get_attribute('href').split('/')[-1] for link in links if 'all-apis' not in link.get_attribute('href')]
	# pprint(endpoints)

	# Always remember to close the browser
	driver.quit()

	return endpoints

apiCategories = fetchLinks('all-apis', '.nav-links__list__level-0-collapsible a[href*="/api/docs/"]')
print('Found ' + str(len(apiCategories)) + ' categories.')
pprint(apiCategories)
print('=' * 50)
for apiCategory in apiCategories:
	print('Scanning Category: ' + apiCategory)
	links = fetchLinks(apiCategory, '.nav-links__list-item__active .nav-links__list__level-2 a[href*="/api/api-ref/"]')
	print('Found ' + str(len(links)) + ' endpoints.')
	pprint(links)
	break

# links = fetchLinks('appointments', '.nav-links__list__level-2 a[href*="/api/api-ref/"]')
# pprint(links)
