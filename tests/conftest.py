import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import allure
import logging

@pytest.fixture(scope='class')
def setup_driver(request: webdriver):
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1280x1024")
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("--headless")
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()

    driver.find_element(By.ID,"user_security_key").send_keys()