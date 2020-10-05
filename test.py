from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("ignore-certificate-errors")
    self.driver = webdriver.Chrome(options=options)
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()
    self.driver.get("https://www.google.com/")
    
