from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ExportDataPage:

    def __init__(self, nwccu):
        self.nwccu = nwccu

    def exportData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Export Data']"))).click()

    def institutionData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Institutional Data']"))).click()

    def programData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Program Data']"))).click()

    def btnBoth(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Both']"))).click()

    def viewExportData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Export Data']")))

    def selAllInstitution(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div/button[2]/span"))).click()

    def delAllInstitution(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div/button[2]/span"))).click()

    def resetAllSelection(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div/button[2]/span"))).click()

    def institutionDataPoints(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[3]/div[1]/div/button[2]"))).click()

    def selDataPoints(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[3]/div[3]/div[1]/div/button[2]/span"))).click()

    def downloadExcelFile(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Download Excel File']"))).click()

    def selAllProgramData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div/button[2]/span"))).click()

    def deselectAllProgramData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div/button[2]/span"))).click()

    def programMetrics(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[4]/div[1]/div/button[2]"))).click()

    def programDemographics(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[4]/div[1]/div/button[3]"))).click()

    def selAllMerticsData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[5]/div[1]/div/button[2]/span"))).click()

    def selAllDemographicsData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div[2]/div/div[1]/div[2]/div[6]/div[1]/div/button[2]/span"))).click()
