from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import xlwt
import time

# Creating the Notebook Object
file_name = 'TextBook.xls'
links_file = 'links.txt'
fileHandle = open(links_file, 'a')
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

# Creating a Driver Object
driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
# Making a Request to the website
driver.get('https://testbook.com/aptitude-practice/')

#res = driver.execute_script('return document.documentElement.innerHTML')
#questionsCategory = driver.find_element_by_css_selector('.panel-body .py-2')
mainPageSource = BeautifulSoup(driver.page_source,'html.parser')

concepts_link = ['https://www.testbook.com'+url.get('href') for url in mainPageSource.select('.panel-body .py-2')]
questionNumber = 1
for i in concepts_link:
    fileHandle.write(i)
    fileHandle.write('\n')
fileHandle.close()
for concept in concepts_link:

        driver.get(concept)
        for i in range(0,25): # here you will need to tune to see exactly how many scrolls you need
            driver.execute_script('window.scrollBy(0, 400)')
            time.sleep(1)
        # Sub page Source
        subPageSource = BeautifulSoup(driver.page_source,'html.parser')
        #time.sleep(5)
        questions_links = ['https://www.testbook.com'+url.get('href') for url in subPageSource.select('.list-view-que-overlay')]

        try:
            for question in questions_links:
                driver.get(question)
                ques = driver.find_element_by_css_selector('body > div.tb-main-content > div.heading-room.practice-container.mb-6.ng-scope.ps-open > div > div:nth-child(2) > div.row.p-relative.zindex-small > div > div:nth-child(2) > div:nth-child(1) > div > div > div > div:nth-child(2)')
                sheet.write(Source_row,Source_col,"TestBook")
                sheet.write(QuestionNumber_row,QuestionNumber_col,questionNumber)
                sheet.write(Question_row,Question_col,ques.text.replace('\n',"\t"))
                #print(ques.text)
                Source_row += 1
                QuestionNumber_row += 1
                Question_row += 1
                questionNumber += 1

                # Dealing with Options
                options = driver.find_element_by_css_selector('.option-content')
                options = [option.text.strip() for option in options]

                sheet.write(OptionNumber_row,OptionNumber_col1,options[0])
                sheet.write(OptionNumber_row,OptionNumber_col2,options[1])
                sheet.write(OptionNumber_row,OptionNumber_col3,options[2])
                sheet.write(OptionNumber_row,OptionNumber_col4,options[3])
                sheet.write(OptionNumber_row,OptionNumber_col5,options[4])

                OptionNumber_row += 1
        except Exception:
            pass
        finally:
            driver.quit()
            excel_file.save(file_name)
#print(questionsCategory.get_attribute(''))

#print(linksList)
driver.quit()