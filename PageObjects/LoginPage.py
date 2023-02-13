from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login:

    def __init__(self,driver):
        self.driver = driver

        self.textbox_username_xpath = "//input[@placeholder='Username']"
        self.textbox_password_xpath = "//input[@placeholder='Password']"
        self.button_submit_xpath = "//button[@type='submit']"
        self.text_invalidmsg_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def input_username(self,Username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(Username)

    def input_password(self,Password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(Password)
    
    def click_submit(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()

    def login_invalid(self):
        return self.driver.find_element(By.XPATH,self.text_invalidmsg_xpath).text