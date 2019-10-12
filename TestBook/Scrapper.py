from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import xlwt
import time

# Creating the Notebook Object
file_name = 'TextBook.xls'
excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('TextBook',cell_overwrite_ok=True)

# Main Constraints
sheet.write(0,0, 'Source')
sheet.write(0,1, 'Test Detail')
sheet.write(0,2, 'Q.No')
sheet.write(0,3, 'Q Text')
sheet.write(0,4, 'Option_1')
sheet.write(0,5, 'Option_2')
sheet.write(0,6, 'Option_3')
sheet.write(0,7, 'Option_4')
sheet.write(0,8, 'Option_5')
sheet.write(0,9, 'Correct Option')
sheet.write(0,10,'Solution Detail')

# Sheet Size Constraints
sheet.col(3).width = 512 * 100
sheet.col(3).height = 512 * 100
sheet.col(0).width = 100 * 50
sheet.col(1).width = 100 * 50
sheet.col(10).width = 512 * 100
sheet.col(10).height = 512 * 100
sheet.col(4).width = 100 * 100
sheet.col(5).width = 100 * 100
sheet.col(6).width = 100 * 100
sheet.col(7).width = 100 * 100
sheet.col(8).width = 100 * 100
sheet.col(9).width = 75 * 75

# Output Data Constraints

# Related to Source
Source_row = 1
Source_col = 0

# Related to Remarks Section
concept_row = 1
concept_col = 1

# Related to Question Number
QuestionNumber_row = 1
QuestionNumber_col = 2


# Related to Question
Question_row = 1
Question_col = 3

# Related to Options
OptionNumber_row = 1
OptionNumber_col1 = 4
OptionNumber_col2 = 5
OptionNumber_col3 = 6
OptionNumber_col4 = 7
OptionNumber_col5 = 8

# Correct options
CorrectOption_row = 1
CorrectOption_col = 9

# Solution List
CorrectSolution_row = 1
CorrectSolution_col = 10

driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')

driver.get('https://testbook.com/aptitude-practice/')
try:
    driver.find_element_by_link_text('Login').click()
    usernameEle = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.NAME, 'emailIDOrUName')))
    print(type(usernameEle))
    print(usernameEle)
except Exception as e:
    print(e)
finally:
    driver.quit()


'''
driver.find_element_by_link_text('Login').click()

res = driver.execute_script('return document.documentElement.innerHTML')

soup = BeautifulSoup(res,'lxml')
#print(soup)
conceptLinks = list()

linksHeader = soup.find_all('div',class_="clearfix topic-list")

for i in linksHeader:
    i = i.find_all('a',class_="py-2 ")
    for j in i:
        conceptLinks.append(j.get('href'))
    

print(conceptLinks)



driver.quit()


'''
'''
try:
    driver.find_element_by_link_text('Login').click()

    username = WebDriverWait(driver,8).until(EC.presence_of_element_located(By.ID,"loginUsername"))
    username.clear()
    username.send_keys('srimani.crypter@gmail.com')
    password = WebDriverWait(driver,8).until(EC.presence_of_element_located(By.NAME,"pswd"))
    password.clear()
    password.send_keys('990306a')
    driver.find_element_by_link_text('Login').click()
except Exception:
    print(Exception)
finally:
    time.sleep(15)
    driver.quit()
'''