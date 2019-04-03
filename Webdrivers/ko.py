from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl
import sys
import os

print('********************* WEATHER - SEARCH  *****************************\nVersion 20181214\n\n Python Syntax: python email-search.py [Excel_worksheet_file_path]\n Exe Syntax: email-search [Excel_worksheet_file_path]')
# if len(sys.argv) > 1:
#     excel_dir = sys.argv[1]
# else:
#     print('Please enter Excel file path as argument')
#     exit()

def wait(driver, seconds):
    print('Waiting',seconds,"seconds . . .")
    driver.implicitly_wait(seconds)
    try:
        driver.find_element_by_css_selector('ligkujgckghvghvukugkljbjhbb87987697g')
    except:
        print("Time's up")

# https://www.ncei.noaa.gov/data/global-hourly/access/
def lookup(driver, station_id, year):
    driver.get("https://www.ncei.noaa.gov/data/global-hourly/access/"+str(year))
    try:
        driver.find_element_by_link_text(station_id+".csv").click()
        print("Saving for ",year)
        year+=1
    except:
        print('nothing')
        quit()
    lookup(driver, station_id, year)
station_id = "72507014765" 
year = 1988
driver = webdriver.Firefox() 
lookup(driver, station_id, year)
print('**************************** WORKSHEET CREATED - NOW OPENING ***********************')
print('Program Complete')