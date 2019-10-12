from selenium import webdriver
from bs4 import BeautifulSoup
import xlwt

# Creating the Notebook Object
file_name = 'FreshersAptitudeTest.xls'
excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('FreshersAptitudeTest',cell_overwrite_ok=True)

# Main Constraints
sheet.write(0,0, 'Source')
sheet.write(0,1, 'Test Detail')
sheet.write(0,2, 'Q.No')
sheet.write(0,3, 'Q Text')
sheet.write(0,4, 'Option_A')
sheet.write(0,5, 'Option_B')
sheet.write(0,6, 'Option_C')
sheet.write(0,7, 'Option_D')
sheet.write(0,8, 'Option_E')
sheet.write(0,9, 'Solution Detail')

# Sheet Size Constraints
sheet.col(3).width = 512 * 100
sheet.col(3).height = 512 * 100
sheet.col(0).width = 100 * 50
sheet.col(1).width = 100 * 50
#sheet.col(9).width = 512 * 100
#sheet.col(9).height = 512 * 100
sheet.col(4).width = 100 * 100
sheet.col(5).width = 100 * 100
sheet.col(6).width = 100 * 100
sheet.col(7).width = 100 * 100
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


# Solution List
#CorrectSolution_row = 1
#CorrectSolution_col = 9


driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')
# Request Count
reqcount = 1
questionCount = 1
try:
    while True:
        driver.get('https://www.fresherslive.com/online-test/aptitude-test/questions-and-answers/{}'.format(reqcount))
        r1 = driver.execute_script('return document.documentElement.outerHTML')
        soup = BeautifulSoup(r1,'lxml')

        questionsList = soup.find_all('div',class_="quslist")
        #print(questionsList)
        # Dealing with Questions
        for i in questionsList:
            i = i.find('div',class_="qus_txt")
            i1 = i.text.split('.')
            l = len(i1[0])+1
            #print(i.text[l:].strip())
            sheet.write(Source_row,Source_col,'FreshersLive')
            sheet.write(concept_row,concept_col,'AptitudeTest-{}'.format(reqcount))
            sheet.write(QuestionNumber_row,QuestionNumber_col,questionCount)
            sheet.write(Question_row,Question_col,i.text[l:].strip())
            Source_row += 1
            concept_row += 1
            QuestionNumber_row += 1
            Question_row += 1
            questionCount += 1
        
        # Dealing with Options

        optionRow = soup.find_all('div',class_="optrow")
            # Creating a new array to store the new results of options
        optionsArray = list()

        for i in optionRow:
            optionsArray.append(i.text.replace('\n','\t').strip())
            
            # Calculating the Length of options Array
        optionsArrayLengthCount = 0
        #print(optionsArray)
        while optionsArrayLengthCount <= len(optionsArray) - 3:
            try:
                optionA,optionB = optionsArray[optionsArrayLengthCount].split('\t')
                optionC,optionD = optionsArray[optionsArrayLengthCount+1].split('\t')
                OptionE = optionsArray[optionsArrayLengthCount+2]
            except Exception:pass
            #print(optionA)
            #print(optionB)
            #print(optionC)
            #print(optionD)
            sheet.write(OptionNumber_row,OptionNumber_colA,optionA.strip())
            sheet.write(OptionNumber_row,OptionNumber_colB,optionB.strip())
            sheet.write(OptionNumber_row,OptionNumber_colC,optionC.strip())
            sheet.write(OptionNumber_row,OptionNumber_colD,optionD.strip())
            sheet.write(OptionNumber_row,OptionNumber_colE,OptionE.strip())
            OptionNumber_row += 1
            optionsArrayLengthCount += 3


        # Deallocating the Memory
        del(optionsArray)       
        '''
        #Dealing with Correct Answer and Solution
        optionsAndAnswers = soup.find_all('div',class_="wholewrap")
        myAnswers = list()
        temp_count = 1
        for sol in optionsAndAnswers:
            sol = sol.find_all('div',class_="explanation")
            for j in sol:
                #print(j.text)
                if(len(j.text.replace('\n','')) > 10):
                    print('{}:'.format(temp_count) + j.text.replace('\n',''))
                    myAnswers.append(j.text.replace('\n',''))
                else:
                    for k in sol:
                        k = k.find_all('div',class_="exp_text")
                        for l in k:
                            print('{}:'.format(temp_count) + l.text.replace('\n',''))
                            myAnswers.append(l.text.replace('\n',' '))

                print(myAnswers[temp_count-1])
                if(len(myAnswers) != temp_count):
                    myAnswers.append('Data Not Extracted')

                temp_count += 1

        
        # Adding Content to the Sheet
        #print(myAnswers)
        for ans in myAnswers:
            explanation = ans.split('Explanation:')
            #print(explanation)
            explanation = explanation[1].strip()
            sheet.write(CorrectSolution_row,CorrectSolution_col,explanation)
            CorrectSolution_row += 1

        del(myAnswers)
        '''
        reqcount += 1
        if(reqcount > 10):
            break
        
    excel_file.save(file_name)
    driver.quit()
except Exception as e:
    print(e)
finally:
    excel_file.save(file_name)
    driver.quit()

    

