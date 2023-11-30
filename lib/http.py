from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

baseUrl = 'https://docs.athenahealth.com/api/docs/'

def fetchLinks(url, handler):
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
	print('Fetching links from: ' + baseUrl + url)
	driver.get(baseUrl + url)

	# Wait for JavaScript to load
	driver.implicitly_wait(10)  # You can adjust the wait time as needed

	# Execute the callback/handler
	handler(driver)

	# Always remember to close the browser
	driver.quit()