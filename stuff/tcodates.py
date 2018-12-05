from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import time
from datetime import datetime, timedelta

date =str(datetime.date.today()).split('-')
year,month,day = date[0],date[1],date[2]

def wait(driver, seconds):
    print('Waiting',seconds,"seconds . . .")
    driver.implicitly_wait(seconds)
    try:
        driver.find_element_by_css_selector('ligkujgckghvghvukugkljbjhbb87987697g')
    except:
        print("Time's up")
driver = webdriver.Firefox() 
driver.get("https://infopost.spectraenergy.com/infopost/NXUSHome.asp?Pipe=NXUS")
Wait(driver, 10)



# driver.switch_to_frame("infoPostFrame")
box = driver.find_element_by_css_selector("body > form > table > tbody > tr > td > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > input[type=\"Text\"]")
box.clear()
box.send_keys("07/28383838383830/2018")

def gen_days( year ):
    start_date = datetime( year, 1, 1 )
    end_date = datetime( year, 12, 31 )
    d = start_date
    dates = [ start_date ]
    while d < end_date:
        d += timedelta(days=1)
        dates.append( d )
    return dates

d = gen_days( 2015 )
print(len(d))
print(d)
d2 = gen_days( 2016 ) # leap year
print(len(d2))