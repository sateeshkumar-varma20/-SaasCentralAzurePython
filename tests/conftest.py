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
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--remote-allow-origins")
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    request.cls.driver = driver
    print("Executing Before Yield.....")
    yield
    print("Executing Yield.....")
    driver.close()
    driver.quit()
