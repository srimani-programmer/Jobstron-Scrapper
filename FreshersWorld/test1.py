import requests
from bs4 import BeautifulSoup
import re
import xlwt

# Creating the Notebook Object
file_name = 'Freshersworld.xls'
excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('Progressions',cell_overwrite_ok=True)

# Main Constraints
sheet.write(0,0, 'Source')
sheet.write(0,1, 'Concept')
sheet.write(0,2, 'Q.No')
sheet.write(0,3, 'Q Text')
sheet.write(0,4, 'Option_A')
sheet.write(0,5, 'Option_B')
sheet.write(0,6, 'Option_C')
sheet.write(0,7, 'Option_D')

# Sheet Size Constraints
sheet.col(3).width = 512 * 125
sheet.col(3).height = 512 * 125
sheet.col(0).width = 100 * 50
sheet.col(1).width = 100 * 100
sheet.col(4).width = 100 * 80
sheet.col(5).width = 100 * 80
sheet.col(6).width = 100 * 80
sheet.col(7).width = 100 * 80


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

questionNumber = 1

req = requests.get('http://placement.freshersworld.com/quantitative-aptitude-questions-and-answers/progression/33111866')
soup = BeautifulSoup(req.text,'lxml')

questions = soup.find_all('div',class_="col-xs-12 col-md-12 content_display mobile_content")
tempList = list()
optionsA = list()
optionsB = list()
optionsC = list()
optionsD = list()
for ques in questions:
    ques = ques.find_all('p')
    for i in ques:
        if(re.search('^[0-9].*\)',i.text) and questionNumber <= 20):
            temp = i.text.split('.')
            if(len(temp) > 2):
                temp = [''.join(temp[x]) for x in range(1,len(temp))]
                sheet.write(Question_row,Question_col,temp[0].strip())
            else:
                temp = temp[1].strip()
                sheet.write(Question_row,Question_col,temp)
            sheet.write(Source_row,Source_col,"Freshers World")
            sheet.write(QuestionNumber_row,QuestionNumber_col,questionNumber)
            sheet.write(concept_row,concept_col,"Progressions")
            Question_row += 1
            questionNumber += 1
            Source_row += 1
            QuestionNumber_row += 1
            concept_row += 1
        else:
            try:
                options = i.text.replace('\xa0','').strip()
                if(options.startswith('a')):
                    options = options.split('.')
                    options = options[1].strip()
                    optionsA.append(options)
                elif(options.startswith('b')):
                    options = options.split('.')
                    options = options[1].strip()
                    optionsB.append(options)
                elif(options.startswith('c')):
                    options = options.split('.')
                    options = options[1].strip()
                    optionsC.append(options)
                elif(options.startswith('d')):
                    options = options.split('.')
                    options = options[1].strip()
                    optionsD.append(options)
            except Exception:pass


for optA,optB,optC,optD in zip(optionsA,optionsB,optionsC,optionsD):
    sheet.write(OptionNumber_row,OptionNumber_colA,optA)
    sheet.write(OptionNumber_row,OptionNumber_colB,optB)
    sheet.write(OptionNumber_row,OptionNumber_colC,optC)
    sheet.write(OptionNumber_row,OptionNumber_colD,optD)
    OptionNumber_row += 1

        
excel_file.save(file_name)
print(tempList)

# Permutations And Combinations
# Surds and Indices
# Profit and Loss
# Time and Work
# Percentages
# Fractions
# Paternerships with slight Modifications
# Progressions ==> ['^[0-9].*\)\.'] ==> Need to work on it.