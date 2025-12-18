from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FiltersPage:

    def __init__(self, nwccu):
        self.nwccu = nwccu

    def dashboardHome(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Dashboard Home']"))).click()

    def institutionType(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']"))).click()

    def institutionAllTypes(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='All types']"))).click()

    def institutionPublic(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='Public']"))).click()

    def institutionPrivateforProfit(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='Private for-profit']"))).click()

    def institutionPrivateNonProfit(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='Private non-profit']"))).click()

    def institution4year(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='4-year']"))).click()

    def institution2year(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='2-year']"))).click()

    def institutionless2year(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='<2-year']"))).click()

    def studentPopulation(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']"))).click()

    def studentPopulationAllSizes(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='All sizes']"))).click()

    def studentPopulation0to500(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']/option[@value='0-500']"))).click()

    def studentPopulation501to1000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']/option[@value='501-1000']"))).click()

    def studentPopulation1001to3000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']/option[@value='1001-3000']"))).click()

    def studentPopulation3001to5000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']/option[@value='3001-5000']"))).click()

    def studentPopulation5001to10000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']/option[@value='5001-10000']"))).click()

    def studentPopulation10001to15000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']/option[@value='10001-15000']"))).click()

    def studentPopulation15001to20000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']/option[@value='15001-20000']"))).click()

    def studentPopulation20000plus(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.studentPopulation']/option[@value='20000+']"))).click()

    def calendarSystem(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.calendarSystem']"))).click()

    def calendarSystemAllSystems(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='All systems']"))).click()

    def calendarSystemSemester(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='Semester']"))).click()

    def calendarSystemQuarter(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='Quarter']"))).click()

    def calendarSystemTrimester(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.institutionType']/option[@value='Trimester']"))).click()

    def deliveryMethod(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.deliveryMethod']"))).click()

    def deliveryMethodAllMethods(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.deliveryMethod']/option[@value='All methods']"))).click()

    def deliveryMethodFullDistance(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.deliveryMethod']/option[@value='Full-Distance']"))).click()

    def deliveryMethodBlended(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.deliveryMethod']/option[@value='Blended']"))).click()

    def deliveryMethodInPerson(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.deliveryMethod']/option[@value='In-Person']"))).click()

    def deliveryMethodFullResidential(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.deliveryMethod']/option[@value='Full-Residential']"))).click()

    def levelofAward(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.levelOfAward']"))).click()

    def levelofAwardAlllevels(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.levelOfAward']/option[@value='All levels']"))).click()

    def levelofAwardCertificate(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.levelOfAward']/option[@value='Certificate']"))).click()

    def levelofAwardDiploma(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.levelOfAward']/option[@value='Diploma']"))).click()

    def levelofAwardAssociate(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.levelOfAward']/option[@value='Associate's']"))).click()

    def levelofAwardBachelor(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.levelOfAward']/option[@value='Bachelor's']"))).click()

    def levelofAwardMaster(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.levelOfAward']/option[@value='Master's']"))).click()

    def levelofAwardDoctoral(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='filters.levelOfAward']/option[@value='Doctoral']"))).click()
  