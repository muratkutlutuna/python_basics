from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

cDriver = webdriver.Chrome("/home/user/Schreibtisch/python_basics/__selenium/chromedriver")
service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
url = "https://sadikturan.com"
driver.get(url)
cDriver.get(url)