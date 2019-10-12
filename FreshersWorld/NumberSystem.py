import requests
from bs4 import BeautifulSoup
import re
import xlwt

# Creating the Notebook Object
file_name = 'Freshersworld.xls'
excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('Number System',cell_overwrite_ok=True)

# Main Constraints
sheet.write(0,0, 'Source')
sheet.write(0,1, 'Concept')
sheet.write(0,2, 'Q.No')
sheet.write(0,3, 'Q Text')
sheet.write(0,4, 'Option_A')
sheet.write(0,5, 'Option_B')
sheet.write(0,6, 'Option_C')
sheet.write(0,7, 'Option_D')
sheet.write(0,8,'Correct Option')

# Sheet Size Constraints
sheet.col(3).width = 512 * 125
sheet.col(3).height = 512 * 125
sheet.col(0).width = 100 * 50
sheet.col(1).width = 100 * 100
sheet.col(4).width = 100 * 80
sheet.col(5).width = 100 * 80
sheet.col(6).width = 100 * 80
sheet.col(7).width = 100 * 80
sheet.col(8).width = 100 * 100


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
OptionNumber_colE = 8

# Correct Option
CorrectOption_row = 1
CorrectOption_col = 8

questionNumber = 1

req = requests.get('http://placement.freshersworld.com/quantitative-aptitude-questions-and-answers/speed-and-distance/33111854')
soup = BeautifulSoup(req.text,'lxml')

questions = soup.find_all('div',class_="col-xs-12 col-md-12 content_display mobile_content")

for ques in questions:
    questions = ques.find_all('li')
    
    for i in questions:
        if(len(i.text.strip()) > 10):
            sheet.write(Source_row,Source_col,"Freshers World")
            sheet.write(QuestionNumber_row,QuestionNumber_col,questionNumber)
            sheet.write(concept_row,concept_col,"Number System")
            sheet.write(Question_row,Question_col,i.text.strip())

            Question_row += 1
            Source_row += 1
            QuestionNumber_row += 1
            questionNumber += 1
            concept_row += 1
        else:
            temp = i.text.split(':')
            temp = temp[1].replace('.','').strip()
            sheet.write(CorrectOption_row,CorrectOption_col,temp.upper())
            CorrectOption_row += 1


    options = ques.find_all('p')
    for opt in options:
        if(opt.text.startswith('a.')):
            opt = opt.text.split(' ')
            optionA = opt[1].replace('\xa0','').strip()
            optionB = opt[3].replace('\xa0','').strip()
            optionC = opt[5].replace('\xa0','').strip()
            optionD = opt[7].replace('\xa0','').strip()
            sheet.write(OptionNumber_row,OptionNumber_colA,optionA)
            sheet.write(OptionNumber_row,OptionNumber_colB,optionB)
            sheet.write(OptionNumber_row,OptionNumber_colC,optionC)
            sheet.write(OptionNumber_row,OptionNumber_colD,optionD)
            OptionNumber_row += 1

excel_file.save(file_name)
            
# Number System
