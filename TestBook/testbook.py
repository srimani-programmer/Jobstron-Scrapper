from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def main():
	
    df = pd.DataFrame(columns=['ques', 'options'])

    url = 'https://testbook.com/aptitude-practice/'

    driver = webdriver.Chrome('/Users/srimanikanta/Downloads/chromedriver')

    driver.get(url)

    sub_cat = driver.find_element_by_css_selector('.topic-list .py-2')

    driver.get(sub_cat.get_attribute('href'))

    for i in range(0,25): # here you will need to tune to see exactly how many scrolls you need
        driver.execute_script('window.scrollBy(0, 400)')
        time.sleep(1)

    page_source = bs(driver.page_source, 'html.parser')

    questions_link = ['https://www.testbook.com'+url.get('href') for url in page_source.select('.list-view-que-overlay')]

    for question in questions_link:
        driver.get(question)

        ques = driver.find_element_by_css_selector('body > div.tb-main-content > div.heading-room.practice-container.mb-6.ng-scope.ps-open > div > div:nth-child(2) > div.row.p-relative.zindex-small > div > div:nth-child(2) > div:nth-child(1) > div > div > div > div:nth-child(2)')

        options = driver.find_elements_by_css_selector('.option-content')

        options = [option.text for option in options]

        df.loc[len(df)] = [ques.text, options]

        print(df.loc[len(df)-1])

        df.to_excel('testbook_cat1_data.xlsx', index=None)

if __name__ == '__main__':
    main()