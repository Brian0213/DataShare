from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    def __init__(self, nwccu):
        self.nwccu = nwccu

    def emailAddress(self, emailaddress):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))).send_keys(emailaddress)

    def setPassword(self, setpassword):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(setpassword)

    def clickSignin(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex items-center justify-center w-full px-4 py-4 space-x-1 text-sm font-semibold leading-4 text-center transition-colors duration-300 bg-blue-600 rounded-md hover:bg-blue-700 text-blue-50']"))).click()

    def clickUploadData(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Upload Data']"))).click()

    def clickApply(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Apply']"))).click()

    def clickReset(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reset']"))).click()

    def registerHere(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Register here']"))).click()

    def regFirstName(self, fname):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='First Name']"))).clear()
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='First Name']"))).send_keys(fname)

    def regLastName(self, lname):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Last Name']"))).send_keys(lname)

    def regRole(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='role']"))).click()

    def regRoleAdmin(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='role']/option[@value='admin']"))).click()

    def regRoleUser(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='role']/option[@value='user']"))).click()

    def regEmailAddress(self, email):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email Address']"))).send_keys(email)

    def regTermsCheckbox(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))).click()

    def regSubmit(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()

    def regCancel(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))).click()

    def regCollegeNameField(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']"))).click()

    def regCollegeBrigham(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='2']"))).click()

    def regCollegeEnsign(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='3']"))).click()

    def regCollegeJoyce(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='4']"))).click()

    def regCollegeNeumont(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='5]"))).click()

    def regCollegeNightingale(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='1']"))).click()

    def regCollegeNoorda(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='6']"))).click()

    def regCollegeRocky(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='7']"))).click()

    def regCollegeSalt(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='8']"))).click()

    def regCollegeSnow(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='9']"))).click()

    def regCollegeSouthern(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='10']"))).click()

    def regCollegeUniversity(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='11']"))).click()

    def regCollegeUtahState(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='12']"))).click()

    def regCollegeUtahTech(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='13']"))).click()

    def regCollegeUtahValley(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='14']"))).click()

    def regCollegeWeber(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='15']"))).click()

    def regCollegeWestern(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='16']"))).click()

    def regCollegeWestminster(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='institution_id']/option[@value='17']"))).click()

    def confirmRegistration(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='px-4 py-3 bg-cyan-900 dark:bg-cyan-950 text-white text-base font-medium rounded-xl hover:bg-cyan-800 dark:hover:bg-cyan-900']"))).click()

    def userMenu(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='text-sm font-medium text-slate-700 dark:text-slate-300']"))).click()

    def userManage(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Manage']"))).click()

    def userSignout(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign Out']"))).click()

    def memberEdit(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div/div/div/div[2]/div/div[2]/table/tbody/tr/td[7]/button[1]"))).click()

    def memberDelete(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div/div[3]/table/tbody/tr[1]/td[8]/button[2]"))).click()

    def btnInstitutions(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Institutions']"))).click()

    def btnAddInstitution(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='+ Add Institution']"))).click()

    def txtCollegeName(self, cname):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(cname)

    def txtWebsite(self, url):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='website']"))).send_keys(url)

    def btnCancel(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))).click()

    def btnCreate(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create']"))).click()

    def btnDeleteInstitution(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div/div[2]/table/tbody/tr[10]/td[3]/button[2]"))).click()

    def deleteInstitution(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Delete']"))).click()

    def btnEditInstitution(self):
        WebDriverWait(self.nwccu, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/main/div/div/div[2]/table/tbody/tr[9]/td[3]/button[1]"))).click()
