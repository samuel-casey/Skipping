def wait(driver, seconds):
    print('Waiting',seconds,"seconds . . .")
    driver.implicitly_wait(seconds)
    try:
        driver.find_element_by_css_selector('ligkujgckghvghvukugkljbjhbb87987697g')
    except:
        print("Time's up")
