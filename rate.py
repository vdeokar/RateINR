from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#driver.get("https://www.remitly.com/us/en/india/pricing")
driver.get("https://www.google.com")
time.sleep(30)

elem = driver.find_element_by_name('Search')
print elem

# username = driver.find_element_by_id()
# password = driver.find_element_by_id()


# username.sendkeys()
# password.sendkeys()

# login_attempt = driver.find_element_by_xpath()

driver.quit()

