from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
import time

import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.fixture
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    request.cls.driver = driver
    request.cls.driver.get(config.get("Urls", "base_url"))
    time.sleep(2)
    yield
    request.cls.driver.quit()