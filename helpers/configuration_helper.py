
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

class ConfigurationHelper:
    def set_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1280x1024")
        options.add_experimental_option('useAutomationExtension', False)
        #options.add_argument("--headless")
        options.add_argument('ignore-certificate-errors')

        # capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        # capabilities['acceptSslCerts'] = True

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)

        driver.get("https://subscription.packtpub.com/login")

