import time
from turtledemo.clock import setup

from selenium import webdriver

from pageObjects.Loginpage import Loginpage
from utilities import ExcelUtils
from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path=".//Testdata/testdata.xlsx"
    logger=LogGen.loggen()

    def test_002_DDT_Login(self ,setup):
        self.logger.info("***********verifying***********")
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        statusAct=[]
        self.Rownum=ExcelUtils.getRowCount(self.path,"Sheet1")
        self.columnnum=ExcelUtils.getColumnCount(self.path,"Sheet1")
        for r in (2,self.Rownum+1):
                username= ExcelUtils.readData(self.path,"Sheet1",r,1)
                password= ExcelUtils.readData(self.path, "Sheet1", r, 2)
                status= ExcelUtils.readData(self.path, "Sheet1", r, 3)
                self.lp.setUserName(username)
                self.lp.setPassword(password)
                self.lp.clickLoginBtn()
                act_title=self.driver.title
                exp_title="Just a moment..."
                if self.driver.title==exp_title:
                    if status=="pass":
                        self.logger.info("***passed***")
                        self.lp.clickLogoutlink()
                        statusAct.append("Pass")
                    elif status=="Fail":
                         self.logger.info("***failed***")
                         statusAct.append("Fail")
                elif act_title!=exp_title:
                    if status=="pass":
                        self.logger.info("***failed***")
                        statusAct.append("Fail")
                    elif status=='Fail':
                        self.logger.info("***passed***")
                        statusAct.append("pass")

        if "Fail" not in statusAct:
            self.logger.info("Login DT not passed...")
        else:
            self.logger.info("*****login DDT test failed***")
