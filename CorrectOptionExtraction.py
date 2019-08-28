from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('https://www.fresherslive.com/online-test/number-system-questions-and-answers')
res = driver.execute_script('return document.documentElement.outerHTML')

optionSet = 21
solutionArray = list()
for i in range(1,optionSet):
    driver.find_element_by_id('optionset{}_1'.format(i)).click()
    driver.find_element_by_id('showans{}'.format(i)).click()
    res = driver.execute_script('return document.documentElement.outerHTML')
    s1 = BeautifulSoup(res,'lxml')
    exp = s1.find_all('div',class_="explanation")

    for i in exp:
        solutionArray.append(i.text.replace('\n',' '))

print(solutionArray[0])
print(solutionArray[-1])
print(solutionArray[15])

driver.quit()