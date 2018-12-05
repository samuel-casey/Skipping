from selenium import webdriver
driver=webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.tccustomerexpress.com/gasdaysummaryreport.html")
driver.maximize_window()
driver.implicitly_wait(30)