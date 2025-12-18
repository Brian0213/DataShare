import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_RegisterMember(BaseTest):

    # email = "oojeyinka@nightingale.edu"
    # fname = "Oluwasegun"
    # lname = "Ojeyinka"
    # role = "Admin"

    def test_login(self, setup):
        self.nwccu = setup
        self.logger.info("******** Verifying Login Test ********")
        self.logger.info("******** Call the Browse Configuration ********")
        self.nwccu.implicitly_wait(10)
        self.logger.info("******** Launch the Application URL ********")
        self.nwccu.get(self.baseURL)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.nwc = LoginPage(self.nwccu)
        windowsIDs = self.nwccu.window_handles
        parentwindowid = windowsIDs[0]
        self.nwc.registerHere()
        self.nwc.regFirstName(self.fname)
        self.nwc.regLastName(self.lname)
        self.nwc.regRole()
        self.nwc.regRoleAdmin()
        self.nwc.regEmailAddress(self.email)
        self.nwc.regCollegeNameField()
        self.nwc.regCollegeNoorda()
        self.nwc.regTermsCheckbox()
        self.nwc.regSubmit()
        # self.nwccu.switch_to.window(parentwindowid)
        time.sleep(5)
        self.nwc.confirmRegistration()






