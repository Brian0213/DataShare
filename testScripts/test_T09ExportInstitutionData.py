import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.ExportDataPage import ExportDataPage
from Pages.FiltersPage import FiltersPage
from Pages.HomePage import HomePage
from Pages.QuickActionsPage import QuickActionsPage
from testScripts.base_test import BaseTest


class Test_ExportInstitutionalData(BaseTest):

    def test_login(self, setup):
        self.nwccu = setup
        self.login(self.nwccu)
        self.logger.info("******** Verifying Login Test ********")
        self.logger.info("******** Define the ExportDataPage Driver ********")
        self.edp = ExportDataPage(self.nwccu)
        self.hp = HomePage(self.nwccu)
        self.logger.info("********Change to Dark Mode ********")
        self.hp.btnDarkLightMode()

        self.logger.info("********Scroll Until the the Export Button is Visible ********")
        self.nwccu.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.nwccu.execute_script("window.scrollBy(0, 2150);")
        self.logger.info("********Select the Export Data Button ********")
        self.edp.exportData()
        self.logger.info("********Select the Institutions Tab ********")
        self.edp.institutionData()
        self.logger.info("********Select the All Institutions Select All Button ********")
        self.edp.selAllInstitution()
        self.logger.info("********Select the Institutions Data Points Tab ********")
        self.edp.institutionDataPoints()
        self.logger.info("********Select the Data Points Select All Button ********")
        self.edp.selDataPoints()
        self.logger.info("********Scroll Until the Download Excel Button is Visible ********")
        self.nwccu.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.logger.info("********Select the Download Excel File Button ********")
        self.edp.downloadExcelFile()

