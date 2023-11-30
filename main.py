from selenium.webdriver.common.by import By
from lib.browser import browse
from lib.specs import fetchSpec
from termcolor import colored

def processCategories(driver):
	categorySelector = '.nav-links__list__level-0-collapsible a[href*="/api/docs/"]'
	endpointSelector = '.nav-links__list-item__active .nav-links__list__level-2 a[href*="/api/api-ref/"]'
	categorySections = driver.find_elements(By.CSS_SELECTOR, categorySelector)
	
	categories = [category.get_attribute('href').split('/')[-1] for category in categorySections if 'all-apis' not in category.get_attribute('href')]
	print('Found %s categories.'% colored(str(len(categories)), 'cyan'))
	for category in categories:
		print('\t' + colored(category, 'green'))

	# Loop through the sections (Skipping the first one) and get the links
	for categorySection in categorySections[1:]:
		# Get the category name
		categoryName = categorySection.get_attribute('href').split('/')[-1]

		# Click the category link
		categorySection.click()

		# Wait for the page to load
		driver.implicitly_wait(10)  # You can adjust the wait time as needed

		# Get all of the endpointSelector links inside the now open accordian
		links = driver.find_elements(By.CSS_SELECTOR, endpointSelector)
	
		endpoints = [link.get_attribute('href').split('/')[-1] for link in links if 'all-apis' not in link.get_attribute('href')]
		print('\nFound %s endpoints in the %s category.' % (colored(str(len(endpoints)), 'cyan'), colored(categoryName, 'green')))
		for endpoint in endpoints:
			print('\t' + colored(endpoint, 'magenta'), end=': ')
			fetchSpec(endpoint, categoryName)

		# Click the category link again to collapse it
		categorySection.click()

# Kick it off, fetch the 'root'
browse('all-apis', processCategories)