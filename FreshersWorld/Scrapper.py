from selenium import webdriver
from bs4 import BeautifulSoup
import xlwt

# Creating the Notebook Object
file_name = 'Freshersworld.xls'
excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('Freshersworld',cell_overwrite_ok=True)

# Main Constraints
sheet.write(0,0, 'Source')
sheet.write(0,1, 'Concept')
sheet.write(0,2, 'Q.No')
sheet.write(0,3, 'Q Text')
sheet.write(0,4, 'Option_A')
sheet.write(0,5, 'Option_B')
sheet.write(0,6, 'Option_C')
sheet.write(0,7, 'Option_D')
sheet.write(0,8, 'Option_E')
sheet.write(0,9, 'Correct Option')
sheet.write(0,10, 'Solution Detail')

# Sheet Size Constraints
sheet.col(3).width = 512 * 100
sheet.col(3).height = 512 * 100
sheet.col(0).width = 100 * 50
sheet.col(1).width = 100 * 50
sheet.col(9).width = 75 * 50
sheet.col(10).width = 512 * 100
sheet.col(10).height = 512 * 100
sheet.col(4).width = 100 * 80
sheet.col(5).width = 100 * 80
sheet.col(6).width = 100 * 80
sheet.col(7).width = 100 * 80
sheet.col(8).width = 100 * 80
sheet.col(9).width = 100 * 100

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

# Correct Answer List
CorrectOption_row = 1
CorrectOption_col = 9

# Solution List
CorrectSolution_row = 1
CorrectSolution_col = 10



driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
driver.get('http://placement.freshersworld.com/quantitative-aptitude-questions-and-answers/33150826')
res = driver.execute_script('return document.documentElement.innerHTML')
soup = BeautifulSoup(res,'lxml')

mainContent = soup.find_all('div',class_="col-md-8 col-xs-12 col-sm-12 category_aptitude_outer")
conceptsLinks = list()
conceptsNames = list()
# Question Number
questionNumber = 1
for i in mainContent:
    i = i.find_all('div',class_="col-md-4 col-sm-4 col-xs-12 list category_content")
    for j in i:
        j = j.find_all('a',class_="link_apt")
        for k in j:
            conceptsLinks.append(k.get('href'))
            conceptsNames.append(k.text.replace('\n','').strip())


sampleCount = 1

for i,j in zip(conceptsLinks,conceptsNames):
    driver.get(i)
    subContent = driver.execute_script('return document.documentElement.innerHTML')
    res1 = BeautifulSoup(subContent,'lxml')
    questionsContent = res1.find_all('div',class_="col-xs-12 col-md-12 content_display mobile_content")

    tempoptionsList = list()
    newoptionsList = list()
    solutionsList = list()
    for options in questionsContent:
        options = options.find_all('p')
        for option in options:
            tempoptionsList.append(option.text)

    for sol in tempoptionsList:
        if(sol.startswith('a.')):
            newoptionsList.append(sol.replace(' ','').strip())
        elif(not sol.startswith('Answer & Explanations') or sol.startswith('') == ''):
            solutionsList.append(sol.strip())

   

    '''
    for opt in newoptionsList:
        print(opt)
    
    for sol in solutionsList:
        print(sol)
    '''
    #sampleCount += 1
    #if(sampleCount > 1):
    #    break


   # To Store the Content of Questions and Correct Options
    questionsList = list()
    newquestionsList = list()
    correctOptionsList = list()
    for ques in questionsContent:
        # Extracting the Questions content and the Correct Options
        ques = ques.find_all('li')
        for con in ques:
            questionsList.append(con.text)
    
    for ques in questionsList:
        if(ques.startswith('Ans:')):
            correctOptionsList.append(ques)
        else:
            newquestionsList.append(ques.strip())
    
    print(newquestionsList)
    #optionsCount = 20
    #for corrt in range(optionsCount,40):
    #    correctOptionsList.append(questionsList[corrt])
    #questionsList = questionsList[0:20]

    for ques,opt,solution in zip(newquestionsList,correctOptionsList,solutionsList):
        sheet.write(Source_row,Source_col,"Freshers World")
        sheet.write(concept_row,concept_col,j)
        sheet.write(QuestionNumber_row,QuestionNumber_col,questionNumber)
        sheet.write(Question_row,Question_col,ques)
        correctOption = opt.split('Ans:')
        correctOption = correctOption[1].replace('.','')
        sheet.write(CorrectOption_row,CorrectOption_col,correctOption.strip())
        sheet.write(CorrectSolution_row,CorrectSolution_col,solution.strip())

        Source_row += 1
        concept_row += 1
        QuestionNumber_row += 1
        Question_row += 1
        questionNumber += 1
        CorrectOption_row += 1
        CorrectSolution_row += 1
    
    questionsList.clear()
    correctOptionsList.clear()
    del(questionsList)
    del(correctOptionsList)
    del(newquestionsList)
    del(newoptionsList)
            
    sampleCount += 1
    if(sampleCount>2):
        break

excel_file.save(file_name)

driver.quit()

