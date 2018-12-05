from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import time

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
driver.get("http://www.columbiapipeinfo.com/infopost/Default.aspx?info=Y")


driver.switch_to_frame("infoPostFrame")
# driver.find_element_by_css_selector("html")
driver.find_element_by_css_selector("body")
wait(driver, 5)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/div/table/tbody/tr[5]/td[2]/span').click()
driver.find_element_by_xpath('//*[@id="6969"]/td[2]/span').click()
wait(driver, 5)
driver.switch_to_frame("mainFrame")
begindate = driver.find_element_by_xpath('//*[@id="ReportViewer1_ctl04_ctl05_txtValue"]')
    # '/html/body/form/div[3]/span/div/table/tbody/tr[1]/td/div/div/table/tbody/tr/td[1]/table/tbody/tr[1]/td[5]/div/div')
# begindate.clear()
wait(driver, 5)
begindate.clear()
wait(driver, 5)
begindate.send_keys("07/20/2018")
# month+"/"+day+"/"+year)
# (Keys.COMMAND + "a")+
driver.find_element_by_xpath("/html/body/form/div[3]/span/div/table/tbody/tr[3]/td/div/div/div[5]/table/tbody/tr/td/div/div[1]/table/tbody/tr/td/input").click()
driver.find_element_by_xpath('//*[@id="ReportViewer1_ctl04_ctl00"]').click()



# driver.quit()