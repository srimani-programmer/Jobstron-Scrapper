from selenium import webdriver
from bs4 import BeautifulSoup

# Establishing a Driver
driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('https://www.fresherslive.com/online-test/number-system-questions-and-answers')
res = driver.execute_script('return document.documentElement.outerHTML')

mainSoup = BeautifulSoup(res,'lxml')

exp = mainSoup.find_all('div',class_="wholewrap")
Array = list()
for i in exp:
    i = i.find_all('div',class_="explanation")
    for j in i:
        Array.append(j.text.replace('\n',''))

print(Array)

driver.quit()