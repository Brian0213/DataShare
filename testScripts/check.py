import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://staging.elportal.nightingale.edu/")

driver.find_element(By.XPATH, "//a[normalize-space()='Click Here to Continue']").click()

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("learner1@learn.nightingale.test")

driver.find_element(By.XPATH, "//input[@name='password']").send_keys("learn1234")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

driver.find_element(By.XPATH, "//span[normalize-space()='My VCBC']").click()

time.sleep(5)