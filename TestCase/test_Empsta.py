import pytest
import time
# from selenium.webdriver import ActionChains

from PageObjects.Dashboard import DashboardPage
from PageObjects.LoginPage import Login
from PageObjects.Emp_status import Emp_status

@pytest.mark.usefixtures("setup")
class TestEmpSts():
    
    def test_empsts(self):
        dp = DashboardPage(self.driver)
        lg = Login(self.driver)
        es = Emp_status(self.driver)
        lg.input_username("Admin")
        lg.input_password("admin123")
        lg.click_submit()

        # ActionChains(self.driver).click(lg.input_password("admin123")).perform()
        # ActionChains(self.driver).click(lg.input_username("Admin")).perform()
        # ActionChains(self.driver).click(lg.click_submit()).perform()

        time.sleep(3)
        dp.click_admin().click()
        time.sleep(3)
        dp.click_job().click()
        time.sleep(3)
        dp.click_emp_status().click()
        time.sleep(3)

        # ActionChains(self.driver).click(es.click_addsts()).perform()
        # time.sleep(2)
        # ActionChains(self.driver).click(es.input_namests("Doe John")).perform()
        # time.sleep(2)
        # ActionChains(self.driver).click(es.click_savasts()).perform()
        # time.sleep(2)
       
        initial_count = 0
        for i in es.count_tablests():
            initial_count = initial_count + 1
        print(initial_count)

        time.sleep(3)
        es.click_addsts()
        time.sleep(3)
        es.input_namests("automation scraping")
        time.sleep(3)
        es.click_savasts()
        time.sleep(6)

        final_count = 0
        for j in es.count_tablests():
            final_count = final_count + 1
        print(final_count)
        time.sleep(3)

        if initial_count + 1 == final_count:
            assert True
        else:
            assert False