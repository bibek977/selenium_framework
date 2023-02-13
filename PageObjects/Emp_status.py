from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Emp_status:

    def __init__(self,driver):
        self.driver = driver

        self.btn_addsts_xpath = "//button[normalize-space()='Add']"
        self.text_namests_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.btn_savests_xpath = "//button[@type='submit']"

        self.count_tablests_xpath = "//div[@class='oxd-table-body']/div[@class='oxd-table-card']"

    def click_addsts(self):
        self.driver.find_element(By.XPATH,self.btn_addsts_xpath).click()

    def input_namests(self,Name):
        self.driver.find_element(By.XPATH, self.text_namests_xpath).send_keys(Name)

    def click_savasts(self):
        self.driver.find_element(By.XPATH, self.btn_savests_xpath).click()

    def count_tablests(self):
        return self.driver.find_elements(By.XPATH,self.count_tablests_xpath)