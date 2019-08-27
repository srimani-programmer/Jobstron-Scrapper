# Importing Libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import xlwt

# Creating the Notebook Object
file_name = 'Day01.xls'
excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('Day01',cell_overwrite_ok=True)

# Main Constraints
sheet.write(0,0, 'Source')
sheet.write(0,1, 'Remarks')
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
Remarks_row = 1
Remarks_col = 1

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

# Setting the Request Count
req_count = 1
# Initialising the Driver Object
driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
Question_Count = 1
Options_Count = 1
while True:
    driver.get('https://www.jobstron.com/aptitude-test-{}'.format(req_count))
    driver.find_element_by_name('startQuiz').click()

    # Response Object
    res = driver.execute_script('return document.documentElement.outerHTML')
    

    # Intialising the Soup Object
    soup = BeautifulSoup(res,'lxml')

    scrapper = list()
    # Question list Extracter.
    
    # Question list
    questions_list = soup.find_all('div', class_="wpProQuiz_question_text")
    # Options List
    options_list = soup.find_all('ul',class_="wpProQuiz_questionList")

    # Dealing with Question Data
    for i in questions_list:
        sheet.write(Source_row,Source_col,'Jobstron')
        sheet.write(Remarks_row,Remarks_col,'Aptitude-Test-{}'.format(req_count))
        sheet.write(QuestionNumber_row,QuestionNumber_col,Question_Count)
        question = str(i.text.replace('\n', '').strip())
        index_val = question.find('.')
        sheet.write(Question_row,Question_col,question[index_val+1:].strip())
        Question_row += 1
        Question_Count += 1
        Source_row += 1
        Remarks_row += 1
        QuestionNumber_row += 1
    
    # Dealing with Options Data

    for i in options_list:
        opt = i.text.replace('\n','').strip().replace(" ", "")
        opt = opt.split(')')
        optionA = opt[1][0:len(opt[1])-1].strip()
        optionB = opt[2][0:len(opt[2])-1].strip()
        optionC = opt[3][0:len(opt[3])-1].strip()
        optionD = opt[4][0:len(opt[4])-1].strip()
        sheet.write(OptionNumber_row,OptionNumber_colA,optionA)
        sheet.write(OptionNumber_row,OptionNumber_colB,optionB)
        sheet.write(OptionNumber_row,OptionNumber_colC,optionC)
        sheet.write(OptionNumber_row,OptionNumber_colD,optionD)
        OptionNumber_row += 1
    

    driver.find_element_by_name('checkSingle').click()

    res = driver.execute_script('return document.documentElement.outerHTML')

    raw_data = BeautifulSoup(res,'lxml')

    # wpProQuiz_response
    correctOption = raw_data.find_all('div',class_="wpProQuiz_incorrect")
   
    # Dealing with Correct Answer 
    for i in correctOption:
        data = i.text.strip()
        data = data.split('Solution:')
        if(len(data) >= 2):
            sheet.write(CorrectOption_row,CorrectOption_col,data[0].strip()[-1].strip())
        else:
            sheet.write(CorrectOption_row,CorrectOption_col,data[0][21])
        CorrectOption_row += 1
    
    # Dealing with Solution

    for i in correctOption:
        data = i.text.strip()
        data = data.split('Solution:')
        if(len(data) >= 2):
            sheet.write(CorrectSolution_row,CorrectSolution_col,data[1].strip())
        else:
            sheet.write(CorrectSolution_row,CorrectSolution_col,data[0][33:].strip())
        CorrectSolution_row += 1

    excel_file.save(file_name) 
    req_count += 1
    if(req_count > 10):
        break


driver.quit()


