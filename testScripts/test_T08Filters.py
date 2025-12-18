import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.FiltersPage import FiltersPage
from Pages.QuickActionsPage import QuickActionsPage
from testScripts.base_test import BaseTest


class Test_Filter(BaseTest):

    def test_login(self, setup):
        self.nwccu = setup
        self.login(self.nwccu)
        self.logger.info("******** Verifying Login Test ********")
        self.logger.info("******** Define the LoginPage Driver ********")
        self.ftr = FiltersPage(self.nwccu)
        self.quk = QuickActionsPage(self.nwccu)

        self.ftr.dashboardHome()
        self.quk.activityLog()

