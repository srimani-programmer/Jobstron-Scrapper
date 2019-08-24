from selenium import webdriver
from bs4 import BeautifulSoup
# import pandas as pd
import xlwt

driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('https://www.jobstron.com/aptitude-test-2')
driver.find_element_by_name('startQuiz').click()

res = driver.execute_script('return document.documentElement.outerHTML')


soup = BeautifulSoup(res,'lxml')

file_name = 'QandAMain.xls'
excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('Sheet1')
scrapper = list()
# Question list Extracter.
count = 1
# Question list
questions_list = soup.find_all('div', class_="wpProQuiz_question_text")
# Options List
options_list = soup.find_all('ul',class_="wpProQuiz_questionList")
# print(type(questions_list))

Qrow = 1
Qcol = 2
Orow = Qrow + 1
Ocol = 2
sheet.write(0,0, 'QNO')
sheet.write(0,1, 'Question')

for i,j in zip(questions_list,options_list):
    sheet.write(Qrow,Qcol,str(i.text.replace('\n', '').strip()))
    Orow = Qrow + 1
    sheet.write(Orow,Ocol,str(j.text.replace('\n','').strip().replace(" ", "")))
    Qrow = Orow + 1


excel_file.save(file_name) 


'''
for i,j in zip(questions_list, options_list):

    scrapper.append(str(i.text.replace('\n', '').strip()))
    print(str(i.text.replace('\n', '').strip()))
    #count += 1
    scrapper.append(str(j.text.replace('\n','').strip().replace(" ", "")))
    print(str(j.text.replace('\n','').strip().replace(" ", "")))
    

df = pd.DataFrame({'Questions and Answers':scrapper})

writer = pd.ExcelWriter('QandA.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()
'''
driver.quit()

#print(options_list[0].text.replace('\n','').strip().replace(' ', ""))

'''
for i in options_list:
    print(i.text.replace('\n','').strip().replace(" ", ""))
'''

