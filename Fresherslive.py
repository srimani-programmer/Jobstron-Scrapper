from selenium import webdriver
from bs4 import BeautifulSoup
import xlwt
import re

# Creating the Notebook Object
file_name = 'FreshersLive.xls'
excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('FreshersLive',cell_overwrite_ok=True)

# Main Constraints
sheet.write(0,0, 'Source')
sheet.write(0,1, 'Concept')
sheet.write(0,2, 'Q.No')
sheet.write(0,3, 'Q Text')
sheet.write(0,4, 'Option_A')
sheet.write(0,5, 'Option_B')
sheet.write(0,6, 'Option_C')
sheet.write(0,7, 'Option_D')
sheet.write(0,8, 'Correct Option')
sheet.write(0,9, 'Solution Detail')

# Sheet Size Constraints
sheet.col(3).width = 512 * 100
sheet.col(3).height = 512 * 100
sheet.col(0).width = 100 * 50
sheet.col(1).width = 100 * 50
sheet.col(8).width = 75 * 50
sheet.col(9).width = 512 * 100
sheet.col(9).height = 512 * 100
sheet.col(4).width = 100 * 50
sheet.col(5).width = 100 * 50
sheet.col(6).width = 100 * 50
sheet.col(7).width = 100 * 50

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
OptionNumber_colA = 4
OptionNumber_colB = 5
OptionNumber_colC = 6
OptionNumber_colD = 7

# Correct Answer List
CorrectOption_row = 1
CorrectOption_col = 8

# Solution List
CorrectSolution_row = 1
CorrectSolution_col = 9


# Storing the Website Constarints
concepts_links = list()
questionsCountValues = list()
concept_names = list()

# Establishing a Driver
driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('https://www.fresherslive.com/online-test/aptitude-test/questions-and-answers')
res = driver.execute_script('return document.documentElement.outerHTML')

mainSoup = BeautifulSoup(res,'lxml')

links = mainSoup.find_all('a',class_="atag_subcat")

# Extracting all Links from the Website
for i in links:
    concepts_links.append(i.get('href'))
    temp = i.find_all('span',class_="sccntspn")
    for j in temp:
        data = j.text
        data = data[1:len(data)-1]
        questionsCountValues.append(data)
    concept = i.find_all('h3',class_="h3subcat")
    for j in concept:
        concept_names.append(j.text.strip())
    

#sample_count = 1
concept_count = 0
questionCount = 1

# Extracting the Data

for i,j in zip(concepts_links,questionsCountValues):
    numberOfPages = int(j)//20
    url = i
    for req in range(1, numberOfPages+2):
        driver.get(url)
        r1 = driver.execute_script('return document.documentElement.outerHTML')
        s1 = BeautifulSoup(r1,'lxml')

        questionsList = s1.find_all('div',class_="quslist")
       # print(questionsList)
        for i in questionsList:
            i = i.find('div',class_="qus_txt")
            sheet.write(Source_row,Source_col,'FreshersLive')
            sheet.write(concept_row,concept_col,concept_names[concept_count])
            sheet.write(QuestionNumber_row,QuestionNumber_col,questionCount)
            i1 = i.text.split('.')
            l = len(i1[0])+1
            sheet.write(Question_row,Question_col,i.text[l:])
            Source_row += 1
            concept_row += 1
            QuestionNumber_row += 1
            questionCount += 1
            Question_row += 1
        try:
            if(req):
                driver.find_element_by_link_text('Next Page').click()
        except Exception:pass
        url = driver.current_url
    concept_count += 1


excel_file.save(file_name)
driver.quit()