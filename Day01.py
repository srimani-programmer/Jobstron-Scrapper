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
    
Ocol = 1
NumberRow = 1
NumberCol = 0


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
        


    '''
    for i,j in zip(questions_list,options_list):
        sheet.write(NumberRow,NumberCol,Question_Count)
        question = str(i.text.replace('\n', '').strip())
        index_val = question.find('.')
        sheet.write(Qrow,Qcol,question[index_val+1:].strip())
        Orow = Qrow + 1
        sheet.write(Orow,Ocol,str(j.text.replace('\n','').strip().replace(" ", "")))
        Qrow = Orow + 1
        NumberRow += 2
        count += 1
    '''


    excel_file.save(file_name) 
    req_count += 1
    if(req_count > 1):
        break


driver.quit()


