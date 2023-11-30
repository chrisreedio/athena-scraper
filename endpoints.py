from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pprint import pprint

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
driver.get('https://docs.athenahealth.com/api/docs/appointments')

# Wait for JavaScript to load
driver.implicitly_wait(10)  # You can adjust the wait time as needed

# Now you can find elements just like in BeautifulSoup
links = driver.find_elements(By.CSS_SELECTOR, '.nav-links__list__level-2 a[href*="/api/api-ref/"]')

endpoints = [link.get_attribute('href') for link in links if 'appointment' in link.get_attribute('href')]
pprint(endpoints)

# Always remember to close the browser
driver.quit()
