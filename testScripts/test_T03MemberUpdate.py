import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_MenuUpdate(BaseTest):

    # fname = "Olu"
    # email = "yinka@nightingale.org"
    # lname = "Oscar"
    # role = "Collaborator"

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
        self.logger.info("******** Click the User's Edit Pen********")
        self.nwc.memberEdit()
        self.logger.info("******** Switch to the Edit Member Window********")
        self.nwccu.switch_to.window(parentwindowid)
        time.sleep(3)
        self.logger.info("******** Edit Member's First Name********")
        self.das.editMemberFirstName(self.fname)
        self.das.editMemberLastName(self.lname)
        self.das.editMemberRole(self.role)
        self.das.editMemberEmail(self.email)
        self.das.editMemberSave()
        # self.nwccu.close()
        # self.logger.info("**********Institution Type Filter Test is Successful********")
        # self.nwccu.find_elements()





