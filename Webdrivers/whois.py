from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl
import sys
import os
def whois(driver, name):
    domain = name[name.index('@')+1:]
    print('DOMAIN:',domain)
    driver.get("https://www.whois.com/whois/"+domain)
    text = driver.find_element_by_tag_name("body").get_attribute("innerText")
    text = text[text.index('Domain Name:'):text.index('Interested in similar domains?')]
    print(text)


driver = webdriver.Firefox() 
name = 'appiispanen@bentley.edu'
whois(driver, name)