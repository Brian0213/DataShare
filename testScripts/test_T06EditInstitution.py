import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_AddInstitution(BaseTest):

    cname = "SpringLake University"
    url = "https://www.sprluni.edu"

    def test_login(self, setup):
        self.nwccu = setup
        self.login(self.nwccu)
        self.logger.info("******** Verifying Login Test ********")
        self.logger.info("******** Define the LoginPage Driver ********")
        self.nwc = LoginPage(self.nwccu)

        self.logger.info("********Verifying Dashboard Pick Lists********")
        self.logger.info("******** Define the HomePage Driver********")
        self.das = HomePage(self.nwccu)
        windowsIDs = self.nwccu.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click the User's Menu********")
        self.nwc.userMenu()
        self.logger.info("******** Click the Manage Button********")
        self.nwc.userManage()
        self.logger.info("******** Click the Institutions Button ********")
        self.nwc.btnInstitutions()
        self.logger.info("******** Click the Institutions Button ********")
        self.nwc.btnEditInstitution()
        self.nwccu.find_element(By.XPATH, "//input[@name='name']").clear()









