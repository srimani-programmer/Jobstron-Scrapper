from selenium import webdriver
from bs4 import BeautifulSoup


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


for i,j in zip(conceptsLinks,conceptsNames):
    driver.get(i)
    subContent = driver.execute_script('return document.documentElement.innerHTML')
    res1 = BeautifulSoup(subContent,'lxml')
    questionsContent = res1.find_all('div',class_="col-xs-12 col-md-12 content_display mobile_content")


    for options in questionsContent:
        options = options.find_all('p')
        for option in options:
            print(option.text)

    for ques in questionsContent:
        # Extracting the Questions content and the Correct Options
        ques = ques.find_all('li')
        for con in ques:
            print(con.text)

    
driver.close()