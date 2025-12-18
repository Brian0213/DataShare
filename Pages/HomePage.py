from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:

    def __init__(self, nwccu):
        self.nwccu = nwccu

    def institutionType(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='inst_type']"))).click()

    def institAny(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='inst_type']/option[@value='Any']"))).click()

    def btnBackHome(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Back to Home']"))).click()

    def btnDarkLightMode(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/header/nav/div/div[2]/button"))).click()

    def institPublic(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='inst_type']/option[@value='Public']"))).click()

    def institPrivateFor(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='inst_type']/option[@value='Private for-profit']"))).click()

    def institPrivateNon(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='inst_type']/option[@value='Private non-profit']"))).click()

    def instit4year(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='inst_type']/option[@value='4-year']"))).click()

    def instit2year(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='inst_type']/option[@value='2-year']"))).click()

    def institless2year(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='inst_type']/option[@value='<2-year']"))).click()

    def calendarSystem(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='calendar_system']"))).click()

    def calAny(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='calendar_system']/option[@value='Any']"))).click()

    def calSemester(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='calendar_system']/option[@value='Semester']"))).click()

    def calQuarter(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='calendar_system']/option[@value='Quarter']"))).click()

    def calTrimester(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='calendar_system']/option[@value='Trimester']"))).click()

    def deliveryMethod(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='delivery_method']"))).click()

    def deliveryAny(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='delivery_method']/option[@value='Any']"))).click()

    def deliveryFullDistance(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='delivery_method']/option[@value='Full-Distance']"))).click()

    def deliveryBlended(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='delivery_method']/option[@value='Blended']"))).click()

    def deliveryFullResidential(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='delivery_method']/option[@value='Full-Residential']"))).click()

    def levelofAward(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='awards']"))).click()

    def awardAny(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='awards']/option[@value='Any']"))).click()

    def awardCertificate(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='awards']/option[@value='Certificate']"))).click()

    def awardDiploma(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='awards']/option[@value='Diploma']"))).click()

    def awardAssociate(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awards"]/option[5]'))).click()

    def awardBachelor(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awards"]/option[6]'))).click()

    def awardMaster(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awards"]/option[7]'))).click()

    def awardDoctoral(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='awards']/option[@value='Doctoral']"))).click()

    def studentPopulation(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']"))).click()

    def studentAny(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='Any']"))).click()

    def student500(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='0-500']"))).click()

    def student1000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='501-1000']"))).click()

    def student3000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='1001-3000']"))).click()

    def student5000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='3001-5000']"))).click()

    def student10000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='5001-10000']"))).click()

    def student15000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='10001-15000']"))).click()

    def student20000(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='15001-20000']"))).click()

    def student20000plus(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='student_pop_range']/option[@value='20000+']"))).click()

    def editMemberFirstName(self, fname):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='first_name']"))).clear()
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='first_name']"))).send_keys(fname)

    def editMemberLastName(self, lname):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='last_name']"))).clear()
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='last_name']"))).send_keys(lname)

    def editMemberRole(self, role):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='role']"))).clear()
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='role']"))).send_keys(role)

    def editMemberEmail(self, email):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))).clear()
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))).send_keys(email)

    def editMemberSave(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()

    def clickHelpTour(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Help Tour']"))).click()

    def btnAddData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()

    def btnDataViews(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()

    def btnTableOrChartView(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()

    def btnFilterData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()

    def btnQuickActions(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()

    def finishSelectInstitutions(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Finish']"))).click()

    def backHelpTour(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Back']"))).click()

    def skipHelpTour(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Skip']"))).click()
