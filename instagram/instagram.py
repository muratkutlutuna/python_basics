from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from instagramUserInfo import username, password
from selenium import webdriver
import time


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        cookiesButton = self.browser.find_element(By.CSS_SELECTOR,"button[class='_a9-- _a9_0']")
        usernameInput = self.browser.find_element(By.XPATH, "(//input[@class='_aa4b _add6 _ac4d'])[1]")
        passwordInput = self.browser.find_element(By.XPATH, "(//input[@class='_aa4b _add6 _ac4d'])[2]")

        cookiesButton.click()
        time.sleep(5)

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)


instagram = Instagram(username,password)
instagram.signIn()