from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DashboardPage:

    def __init__(self,driver):
        self.driver = driver

        self.textbox_welcome_xpath = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"
        self.admin_xpath = "//span[normalize-space()='Admin']"
        self.job_xpath = "//span[normalize-space()='Job']"
        self.emp_status_xpath = "//a[normalize-space()='Employment Status']"

    def text_welcome(self):
        return self.driver.find_element(By.XPATH,self.textbox_welcome_xpath).text

    def click_admin(self):
        return self.driver.find_element(By.XPATH,self.admin_xpath)

    def click_job(self):
        return self.driver.find_element(By.XPATH,self.job_xpath)

    def click_emp_status(self):
        return self.driver.find_element(By.XPATH,self.emp_status_xpath)