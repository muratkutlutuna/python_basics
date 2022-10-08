from selenium import webdriver
import time


driver = webdriver.Chrome("/home/user/Schreibtisch/python_basics/__selenium/chromedriver")


url = "http://github.com"
driver.get(url)

time.sleep(2)
print(driver.title)
driver.maximize_window()
driver.save_screenshot("github.png")

url = "http://github.com/muratkutlutuna"
driver.get(url)

print(driver.title)
if "kutlu" in driver.title:
    driver.save_screenshot("kutlu.png")

time.sleep(2)
driver.back()

time.sleep(2)
driver.close()