from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('https://www.fresherslive.com/online-test/number-system-questions-and-answers')
res = driver.execute_script('return document.documentElement.outerHTML')

soup = BeautifulSoup(res,'lxml')

optionRow = soup.find_all('div',class_="optrow")
temp = list()
for i in optionRow:
    temp.append(i.text.replace('\n','\t').strip())

print(temp)
driver.quit()