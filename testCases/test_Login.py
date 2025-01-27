import time

import pytest
from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_homepageTitle(self,setup):
        self.logger.info("***************testcase_id 0001*****************")
        self.logger.info("***************verifying Homepage title*****************")
        self.logger.info("***************started*****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title=self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("***************testcase is passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\", "test_homepageTitle")
            self.logger.error("**********************testcase is failed*****************")
            assert False

    def test_login(self,setup):
        self.logger.info("***************testcase_id 002*****************")
        self.logger.info("***************verifying Login*****************")
        self.logger.info("***************started*****************")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        act_title=self.driver.title
        time.sleep(2)
        if act_title.__contains__("Just a moment..."):
            assert True
            self.driver.close()
            self.logger.info("***************Testcase passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\","test_login")
            self.driver.close()
            self.logger.error("***************Testcase failed*****************")
            assert False


        time.sleep(15)

