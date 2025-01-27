import time

from selenium import webdriver
driver=webdriver.Chrome()

def test_pythlaunchingBrowser():
    driver.get("https://admin-demo.nopcommerce.com/Admin")
    time.sleep(5)
