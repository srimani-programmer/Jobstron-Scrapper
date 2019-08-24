from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('https://www.jobstron.com/aptitude-test-2')

res = driver.execute_script('return document.documentElement.outerHTML')

soup = BeautifulSoup(res,'lxml')

scrapper = list()
# Question list Extracter.
count = 1
# Question list
questions_list = soup.find_all('div', class_="wpProQuiz_question_text")
# Options List
options_list = soup.find_all('ul',class_="wpProQuiz_questionList")
# print(type(questions_list))
for i in range(questions_list):
    scrapper.append('{}'.format(count) + questions_list[i].text.replace('\n', '').strip())
    count += 1
    scrapper.append(options_list[i].text.replace('\n','').strip().replace(" ", ""))

driver.quit()

df = pd.DataFrame({'Questions and Answers':scrapper})

writer = pd.ExcelWriter('QandA.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()

#print(options_list[0].text.replace('\n','').strip().replace(' ', ""))

'''
for i in options_list:
    print(i.text.replace('\n','').strip().replace(" ", ""))
'''
