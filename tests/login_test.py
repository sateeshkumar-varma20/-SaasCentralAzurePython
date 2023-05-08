import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

@pytest.mark.usefixtures("setup_driver")
class TestSaasLoginPage:

    def test_login(self):
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        log.info("Launch Application")
        self.driver.get("https://dev-sascental.azurewebsites.net/userlogin")
        # allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=AttachmentType.PNG)
        self.driver.maximize_window()
        screenshot_file = "./Screenshots/screenshot{0}.png".format(str(random.randint(0, 100)))
        print(screenshot_file)
        self.driver.save_screenshot(screenshot_file)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user_security_key"))
        )
        self.driver.find_element(By.ID, "user_security_key").send_keys("RGP3PG")
        self.driver.find_element(By.ID, "user_emai_id").send_keys("man11111ish+831_s3@gmail.com")
        self.driver.find_element(By.ID, "user_password").send_keys("12345")
        self.driver.find_element(By.XPATH, "//span[text()='Sign In']/..").click()
        time.sleep(5)
        #//mat-icon[contains(text(),'account_circle')]/../..']/..
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "nito-plus-profile"))
        )
        self.driver.find_element(By.ID, "nito-plus-profile").click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "button-sign-out"))
        )
        self.driver.find_element(By.ID, "button-sign-out").click()
        time.sleep(5)

