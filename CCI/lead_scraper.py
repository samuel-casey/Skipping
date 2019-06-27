 # # # # # # # # # # #  RELATIONSHIP WEB DRIVER # # # # # # # # # # # # 
 # # # # # #  Webdriver for finding relationships to cond_treat # # # # 

"""
How to get data: 

    1. Query Natural treatments for __[condition]__:
    2. Copy Bullets
    3. Match treatment with ID or add new one
    4. Add condition/treatment ID to treat_cond 
    
"""

import sys, csv, re
sys.path.insert(0, 'C:\\Users\\apiispanen\\Desktop\\pyscripts\\Tools')
from scraper import *
print('********************* CCI Lead Maker *****************************\n APP - Version 20190619\n\n*************************')

# 1  - Query w/ webdriver to Duckduckgo
i=0

def get_result_css(i):
    result_css = '#r1-'+str(i)+' > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1)'
    return result_css
def get_queries_list():
    location = "ref_lists\\possible_queries.csv"
    with open(location, newline='') as csvfile:
        query_reader = csv.reader(csvfile)
        queries_list = [row[0].lower() for row in query_reader]
    return queries_list

query_list = get_queries_list()
enter_record(['Email'], 'Source URL')
driver = get_driver()
driver.get('https://duckduckgo.com/?q=test')
duck_duck_scroll(driver)
full_mail_list = []
for query in query_list:
    url = 'https://duckduckgo.com/?q='+query+'&t=hi&ia=web'
    print("new query - "+query)
    for i in range(1,150):
        driver.get(url)
        wait(driver,2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if try_to_click(driver, get_result_css(i)):
            try:        
                text = driver.find_element_by_tag_name("body").text.replace('\n',' ')
                temp_mail_list = re.findall('\w+@\w+\.{1}\w+',text)
                print(i, temp_mail_list)
                full_mail_list.extend(temp_mail_list)
                current_url = driver.current_url
                enter_record(temp_mail_list, current_url)
            except: 
                print("Something went wrong with text stuff")
                driver.get(url)
        else:
            print("Tried, but did not find results....")
            break
print(full_mail_list)