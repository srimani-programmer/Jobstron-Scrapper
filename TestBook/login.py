from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')

driver.get('https://testbook.com/aptitude-practice/')

driver.find_element_by_link_text('Login').click()

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "loginUsername")))
    user = driver.find_element_by_id('loginUsername')
    user.clear()
    user.send_keys('srimani.crypter@gmail.com')
except Exception:print(Exception)
finally:
    driver.quit()