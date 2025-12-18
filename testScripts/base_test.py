import time
from Pages.LoginPage import LoginPage
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class BaseTest:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    fname = ReadConfig.get_fname()
    lname = ReadConfig.get_lname()
    email = ReadConfig.get_email()
    role  = ReadConfig.get_role()

    logger = LogGen.loggen()

    def login(self, driver):
        self.logger.info("****** Starting login ******")
        driver.implicitly_wait(10)
        driver.get(self.baseURL)
        login_page = LoginPage(driver)
        login_page.emailAddress(self.username)
        login_page.setPassword(self.password)
        login_page.clickSignin()
        self.logger.info("****** Login successful ******")
