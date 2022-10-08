from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/home/user/Schreibtisch/python_basics/__selenium/chromedriver")

url = "http://github.com"
driver.get(url)

searchInput = driver.find_element(By.NAME, "q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_elements(By.CSS_SELECTOR, ".repo-list-item div div div a")

for element in result:
    print(element.text)

driver.close()
