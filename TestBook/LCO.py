from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('https://learncodeonline.in/')

driver.find_element_by_link_text('Login').click()
userid = driver.find_element_by_id('lernystLogin_new_user_user_email')
userid.clear()
userid.send_keys('srimanikantapalakollu@gmail.com')
password = driver.find_element_by_id('lernystLogin_new_user_user_password')
password.clear()
password.send_keys('990306@Jesus')
time.sleep(3)
driver.find_element_by_id('lr_login_btn').click()

time.sleep(20)
driver.quit()