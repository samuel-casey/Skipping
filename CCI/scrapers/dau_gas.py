from scraper import get_driver, wait, try_to_click

url = 'https://ebb.dcpmidstream.com/ipws/#/infopost/crp'
download_dir = r'V:\Gas_Qual\MW\CIM'
items_to_click_list = [
    '#top-pane > div:nth-child(1) > div > div.sg-well > div > div > ul > li:nth-child(2) > ul > li:nth-child(2) > div > span > span:nth-child(2)',
    '#aria_active_cell > span',
    '#aria_active_cell > input'
    ]


driver = get_driver()

###                 STEP 1 - GET URL                ###
driver.get(url)
###            STEP 2 - CLICK ON RELEVANT THINGS    ###

for item in items_to_click_list:
    if type(item) != list:
        print("trying to click")
        try_to_click(driver, item, five_sec_retries = 10)
    else:
        driver.find_element_by_css_selector(item[0]).sendkeys(item[1])

###            LAST STEP - CLOSE EVERYTHING         ###
wait(driver, 2)
driver.close()