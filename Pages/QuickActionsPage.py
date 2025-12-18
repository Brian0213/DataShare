from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class QuickActionsPage:

    def __init__(self, nwccu):
        self.nwccu = nwccu

    def activityLog(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div/aside/div[2]/div/a[1]/span"))).click()

    def uploadTemplate(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Upload Template']"))).click()

    def manualDataEntry(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Manual Data Entry']"))).click()

    def exportData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Export Data']"))).click()

    def addData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add Data']"))).click()

    def institutionPublic(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='Public']"))).click()

    def institutionPrivateforProfit(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='Private for-profit']"))).click()
