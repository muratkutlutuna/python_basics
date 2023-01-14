from selenium.webdriver.common.by import By

from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.username = username
        self.password = password
        self.a = ActionChains(self.browser)

    def signIn(self):
        self.browser.get("https://twitter.com/")
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//span[text()='Accept all cookies']").click()
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//span[text()='Log in']").click()
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//input[@name='text']").send_keys(self.username)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//span[text()='Next']").click()
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//input[@name='password']").send_keys(self.password)
        self.browser.implicitly_wait(10)
        m = self.browser.find_element(By.CSS_SELECTOR, "div[data-testid='LoginForm_Login_Button']")
        self.a.move_to_element(m).perform()
        time.sleep(4)
        self.browser.find_element(By.CSS_SELECTOR, "div[data-testid='LoginForm_Login_Button']").click()
        self.browser.implicitly_wait(10)
        time.sleep(4)

    def signOut(self):
        time.sleep(4)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.CSS_SELECTOR, "div[aria-label='Account menu']").click()
        self.browser.implicitly_wait(10)
        time.sleep(4)
        self.browser.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
        self.browser.implicitly_wait(10)
        time.sleep(4)
        self.browser.find_element(By.CSS_SELECTOR, "div[data-testid='confirmationSheetConfirm']").click()
        time.sleep(10)


    def closeBrowser(self):
        self.browser.quit()


twitter = Twitter(username, password)

# login
twitter.signIn()
twitter.signOut()
twitter.closeBrowser()
