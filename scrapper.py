from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('https://www.jobstron.com/aptitude-test-2')

res = driver.execute_script('return document.documentElement.outerHTML')

soup = BeautifulSoup(res,'lxml')

# Question list Extracter.
count = 1
questions_list = soup.find_all('div', class_="wpProQuiz_question_text")
for i in questions_list:
    print('{}'.format(count) + i.text.replace('\n', '').strip())
    count += 1
driver.quit()