import time
import sys
import pytest
from selenium.webdriver.common.by import By


from Pages.HomePage import HomePage
from testScripts.base_test import BaseTest


class Test_Help_Tour(BaseTest):

    def test_login(self, setup):
        self.nwccu = setup
        self.login(self.nwccu)
        self.logger.info("******** Verifying Login Test ********")
        self.logger.info("******** Define the HomePage Driver ********")
        self.hop = HomePage(self.nwccu)

        self.logger.info("******** Click the Help Tour Button ********")
        self.hop.clickHelpTour()
        windowsIDs = self.nwccu.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("********Switch to the Help Tour Feature********")
        self.nwccu.switch_to.window(parentwindowid)
        self.logger.info("********Click the Add Data Modal's Next button********")
        self.hop.btnAddData()
        self.logger.info("********Click Data View's Next button********")
        self.hop.btnDataViews()
        self.logger.info("********Click Table or Chart View's Next button********")
        self.hop.btnTableOrChartView()
        self.logger.info("********Click Filter Data's Next button********")
        self.hop.btnFilterData()
        self.logger.info("********Click Quick Actions' Next button********")
        self.hop.btnQuickActions()
        self.logger.info("********Click Select Institution's Finish button********")
        self.hop.finishSelectInstitutions()
        self.logger.info("******** Close the Browser********")
        self.nwccu.close()
        self.logger.info("**********Help Tour Test is Successful********")

