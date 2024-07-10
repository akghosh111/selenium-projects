from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'English')]"
))
)

language = driver.find_element(By.XPATH,"//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)
#cookie.click()

time.sleep(10)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text
    print(cookies_count)