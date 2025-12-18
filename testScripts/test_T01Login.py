import time
import sys
import os
import pytest
from testScripts.base_test import BaseTest


class Test_Login_NWCCU(BaseTest):

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.nwccu= setup
        self.login(self.nwccu)
        self.logger.info("******** Login Test is successful ********")
        act_title = self.nwccu.title
        self.logger.info("******** Assert Page Title ********")
        if act_title == "Data Sharing Platform":
            assert True
            self.nwccu.close()
        else:
            self.nwccu.save_screenshot("/Users/OluwasegunOjeyinka/PycharmProjects/NWCCU/Screenshots/Failed.png")
            self.nwccu.close()
            assert False
        self.logger.info("Login Test is successful and assertion passed")







































        # self.logger.info("******** Verifying Login Test ********")
        # self.logger.info("******** Call the Browse Configuration ********")
        # self.nwccu.implicitly_wait(10)
        # self.logger.info("******** Launch the Application URL ********")
        # self.nwccu.get(self.baseURL)
        # self.logger.info("******** Define the LoginPage Driver ********")
        # self.nwc = LoginPage(self.nwccu)
        # time.sleep(3)
        # self.logger.info("******** Enter the Username ********")
        # self.nwc.emailAddress(self.username)
        # time.sleep(3)
        # self.logger.info("******** Enter the Password ********")
        # self.nwc.setPassword(self.password)
        # time.sleep(3)
        # self.logger.info("******** Click the Sign in Button********")
        # self.nwc.clickSignin()
        # time.sleep(5)