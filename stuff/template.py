from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import time

def wait(driver):
    try:
        driver.find_element_by_css_selector('null')
    except:
        print('waited')
driver = webdriver.Firefox() 
driver.get("http://www.columbiapipeinfo.com/infopost/Default.aspx?info=Y")
driver.implicitly_wait(5)

