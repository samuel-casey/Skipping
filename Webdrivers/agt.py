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
    driver.get("https://infopost.spectraenergy.com/infopost/AGHome.asp?Pipe=AG")
    try:
        driver.find_element_by_link_text("Capacity").click()
        print("clicked capacity")
        driver.find_element_by_link_text("Operationally Available").click()
        print("clicked capacity")
        wait(driver, 5)
        driver.switch_to.frame(driver.find_element_by_css_selector("#ddlSelector"))
        print("cicked cycle bar")
        driver.find_element_by_css_selector("#ddlSelector > option:nth-child(1)")
        print("found frame")
        for i in range(38):
            print(i)
            driver.find_element_by_css_selector("#ddlSelector > option:nth-child("+str(i)+")")
            print("clicked i",i)
        #ctl00_MainContent_UpdatePanel1
        #ContentPaneIframe
            driver.find_element_by_link_text("Downloadable Format").click()
        print("Saving for ",year)
        year+=1
    except:
        print('nothing')
        quit()
    lookup(driver, station_id, year)
station_id = "72507014765" 
year = 2018
driver = webdriver.Firefox() 
lookup(driver, station_id, year)
print('**************************** WORKSHEET CREATED - NOW OPENING ***********************')
print('Program Complete')