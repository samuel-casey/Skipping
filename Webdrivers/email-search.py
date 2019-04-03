from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl
import sys
import os

print('********************* EMAIL - SEARCH  *****************************\nVersion 20181211\n\n Python Syntax: python email-search.py [Excel_worksheet_file_path]\n Exe Syntax: email-search [Excel_worksheet_file_path]')
if len(sys.argv) > 1:
    excel_dir = sys.argv[1]
else:
    print('Please enter Excel file path as argument')
    exit()

def wait(driver, seconds):
    print('Waiting',seconds,"seconds . . .")
    driver.implicitly_wait(seconds)
    try:
        driver.find_element_by_css_selector('ligkujgckghvghvukugkljbjhbb87987697g')
    except:
        print("Time's up")

def lookup(driver, name):
    driver.get("https://duckduckgo.com/?q="+name+"&ia=web")
    driver.find_element_by_css_selector("#r1-0 > div:nth-child(1) > h2:nth-child(1)").click()
    text = driver.find_element_by_tag_name("body").get_attribute("innerText")
    print(text)
    return text

def whois(driver, name):
    domain = name[name.index('@')+1:]
    print('DOMAIN:',domain)
    driver.get("https://www.whois.com/whois/"+domain)
    text = driver.find_element_by_tag_name("body").get_attribute("innerText")
    try:
        text = text[text.index('Domain Name:'):text.index('Interested in similar domains?')]
    except:
        print(name,"*****WHOIS WEBPAGE FORMAT DIFFERENT")
    print(text)
    return text
driver = webdriver.Firefox() 
wb = openpyxl.load_workbook(excel_dir)
# os.chdir('C:\\Users\\apiispanen\\Desktop\\SCRIPTS')
sheet = wb.get_sheet_by_name(wb.get_sheet_names()[0])
stop = False
i = 0
while stop == False:
    if sheet['A'+str(2+i)].value is not None:
        i+=1
        continue
    else:
        stop=True
truecount=i #HOW MANY ENTRIES YOU GOT???
print("Count of rows present:",i)
for i in range (truecount): 
    code = sheet['A'+str(2+i)].value
    val = lookup(driver, code)
    sheet['C'+str(2+i)] = val
    sheet['B'+str(2+i)] = driver.current_url
    sheet['D'+str(2+i)] = whois(driver, code)
    wait(driver,2)
wb.save('lookup2.xlsx')
print('**************************** WORKSHEET CREATED - NOW OPENING ***********************')
os.startfile('lookup2.xlsx')
print('Program Complete')