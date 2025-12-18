import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_InstitutionType(BaseTest):

    def test_login(self, setup):
        self.nwccu = setup
        self.login(self.nwccu)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.nwc = LoginPage(self.nwccu)
        self.logger.info("********Verifying Institution Type Filter Test ********")
        self.logger.info("******** Define the Job Driver********")
        self.das = HomePage(self.nwccu)
        windowsIDs = self.nwccu.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("********Click the Institution Type Field********")
        self.das.institutionType()
        self.logger.info("********Select the Institution Type's Pick Option********")
        self.das.institPublic()
        self.logger.info("********Click the Student Population Field********")
        self.das.studentPopulation()
        self.logger.info("********Select the Student Population's Pick Option********")
        self.das.student10000()
        self.logger.info("********Click the Delivery Method Field********")
        self.das.deliveryMethod()
        self.logger.info("********Select the Delivery Method's Pick Option********")
        self.das.deliveryFullResidential()
        self.logger.info("********Click the Level of Award Field********")
        self.das.levelofAward()
        self.logger.info("********Select the Level of Award's Pick Option********")
        self.das.awardCertificate()
        self.logger.info("********Click the Apply Button********")
        # self.das.buttonReset()
        self.logger.info("******** Close the Browser********")
        self.nwccu.close()
        self.logger.info("**********Institution Type Filter Test is Successful********")




