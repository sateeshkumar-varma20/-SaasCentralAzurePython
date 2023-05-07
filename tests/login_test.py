import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
import logging

@pytest.mark.usefixtures("setup_driver")
class TestDemo:

    def test_login(self):
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        log.info("Launch Application")
        self.driver.get("https://subscription.packtpub.com/login")
        allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=AttachmentType.PNG)
        self.driver.maximize_window()

