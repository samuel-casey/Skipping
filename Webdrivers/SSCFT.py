from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
# import wkhtmltopdf
# import datetime
# import time
# from datetime import datetime, timedelta

# date =str(datetime.date.today()).split('-')
# year,month,day = date[0],date[1],date[2]

def wait(driver, seconds):
    print('Waiting',seconds,"seconds . . .")
    driver.implicitly_wait(seconds)
    try:
        driver.find_element_by_css_selector('ligkujgckghvghvukugkljbjhbb87987697g')
    except:
        print("Time's up")
driver = webdriver.Firefox() 
driver.get("https://csimain.sscgp.com/App/InformationalPostings/TransactionalReporting/TransactionalReportingFirmTransportation")
#HELP
# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2) # custom location 
# profile.set_preference('browser.download.manager.showWhenStarting', False) 
# profile.set_preference('browser.download.dir', '/tmp') 
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
# END HELP

# SET THE LOOP BELOW:
loop = 10

driver.switch_to_frame("CSIMain")
for i in range(loop):
    xpath = "//*[@id=\"wdgEBBPostings_it5_"+str(i)+"_lnkViewEBBPostings\"]"
    link = driver.find_element_by_xpath(xpath).click()
    wait(driver, 5)
    url = driver.current_url
    # pdfkit.from_url(url, '')
    # wkhtmltopdf.wkhtmltopdf(url=url, output_file='C:\\Users\\apiispanen\\Documents\\Scraper\\out.pdf')
driver.close()

# def gen_days( year ):
#     start_date = datetime( year, 1, 1 )
#     end_date = datetime( year, 12, 31 )
#     d = start_date
#     dates = [ start_date ]
#     while d < end_date:
#         d += timedelta(days=1)
#         dates.append( d )
#     return dates

# d = gen_days( 2015 )
# print(len(d))
# print(d)
# d2 = gen_days( 2016 ) # leap year
# print(len(d2))