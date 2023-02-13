import time
import pytest

# import sys
# sys.path.append("/home/bibek/projects/selenium_framework")

from PageObjects.Dashboard import DashboardPage
from PageObjects.LoginPage import Login

from Utilities.logger import Logclass

import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.mark.usefixtures('setup')
class TestLogIn(Logclass):
    
    def test_001(self):
        
        log = self.getlogs()

        dp = DashboardPage(self.driver)
        lg = Login(self.driver)

        log.info("Test Case started")
        log.info("Test Case 001")

        lg.input_username(config.get("Credentials", "real_username"))
        log.info("Username entered")

        lg.input_password(config.get("Credentials", "real_password"))
        log.info("Password Entered")

        lg.click_submit()
        log.info("Login button clicked")

        time.sleep(2)
        if "Dashboard" == dp.text_welcome():
            self.driver.save_screenshot("Screenshot/Testlogin_001.png")
            assert True
            log.info("Login Successful")
        else:
            self.driver.save_screenshot("Screenshot/Testlogin_001.png")
            log.critical("Login Failed")
            assert False


    def test_002(self):
        lg = Login(self.driver)
        lg.input_username(config.get("Credentials", "fake_username"))
        lg.input_password(config.get("Credentials", "real_username"))
        lg.click_submit()
        time.sleep(2)
        if "Invalid credentials" == lg.login_invalid():
            assert True
        else:
            assert False


    def test_003(self):
        lg = Login(self.driver)
        lg.input_username(config.get("Credentials", "real_username"))
        lg.input_password(config.get("Credentials", "fake_username"))
        lg.click_submit()
        time.sleep(2)
        if "Invalid credentials" == lg.login_invalid():
            assert True
        else:
            assert False
