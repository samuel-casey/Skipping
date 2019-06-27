 # # # # # # # # # # #  RELATIONSHIP WEB DRIVER # # # # # # # # # # # # 
 # # # # # #  Webdriver for finding relationships to cond_treat # # # # 

"""
How to get data: 

    1. Query Natural treatments for __[condition]__:
    2. Copy Bullets
    3. Match treatment with ID or add new one
    4. Add condition/treatment ID to treat_cond 
    
"""
from selenium import webdriver
from analyze import return_viable_treatments, get_treatment_list, get_conditions_dict
from emailer import send_email
def driver_initialize():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.privatebrowsing.autostart", True)    
    driver = webdriver.Firefox(firefox_profile=profile) 
    return driver
print('********************* T_C Relationship Maker *****************************\n APP - Version 20190621\n\n*************************')

treatment_categories = ['supplements', 'food and drinks','alternative therapies']
condition_dict = get_conditions_dict()
treatment_list = get_treatment_list()


######### ITERATOR FOR SEARCH RESULTS ######

def generate_search_output(driver, treatment_category, condition, condition_category, treatment_list, output = 'output.csv'):
    def wait(driver, seconds):
        print('Waiting '+str(seconds)+" seconds . . .")
        driver.implicitly_wait(seconds)
        try:
            driver.find_element_by_css_selector('ligkujgckghvghvukugkljbjhbb87987697g')
        except:
            print("Time's up")    
    def enter_record(results_list, url, condition_category, condition, output = "output.csv"):
        for result in results_list:    
            with open(output, 'a') as file:
                file.write(condition+","+result+","+condition_category+","+url+","+str(len(results_list))+'\n')
            file.close()    
    print("#### LOOKING FOR "+condition+" "+treatment_category)
    for i in range(1,15):
        #### DEFINE VARIABLES ####
        result_number, tries = i, 0
        url, result_css = 'https://scinapse.io/search?query='+treatment_category+'%20for%20'+condition+'&sort=RELEVANCE&filter=year%3D%3A%2Cfos%3D%2Cjournal%3D&page=1', '#react-app > div > div:nth-child(2) > div > div.articleSearch_articleSearchContainer_2tjPz > div.articleSearch_innerContainer_2SzxY > div.searchList_searchItems_1sdxw > div:nth-child('+str(result_number)+') > div > div:nth-child(1) > a.title_title_2TG0L' #,'span.desktopPagination_pageItem_1pyH2:nth-child(', ')'
        if i >= 11:
            url, result_css = 'https://duckduckgo.com/?q=%22webmd%22+%22nih%22+'+treatment_category+'+for+'+condition+'&t=hi&ia=web', '#r1-'+str(i-11)+' > div > h2 > a.result__a'
        #### THIS IS THE ALGORITHM ####
        driver.get(url)
        wait(driver, 2)
        failure = False
        try:
            driver.find_element_by_css_selector(result_css).click()
            print(str(result_number)+"# RESULT FOUND")
        except:
            print(" Try is a failure, result_num is "+str(result_number))
            failure =  True
        try:
            if not failure: 
                text = driver.find_element_by_tag_name("body").text.replace('\n',' ')
                viable_treatments = return_viable_treatments(text,treatment_list)
                url = driver.current_url 
                print(str(i)+": "+url, viable_treatments)
                enter_record(viable_treatments, url, condition_category, condition, output=output)
        except:
            print("something failed with the text")

### IGNORE THIS FOR NOW ###
iteration, two_hund = 0, 0
####


driver = driver_initialize()
###### THIS IS THE MAIN LOOOPPPPPP #########
for condition in condition_dict:
    condition_category = condition_dict[condition]
    for treatment_category in treatment_categories:
        generate_search_output(driver, treatment_category, condition, condition_category, treatment_list)
        iteration += 1
#####       MAIN LOOP OVER         #########

        #### IGNORE BELOW FOR NOW ###
        if iteration > 50:
            iteration = 0
            two_hund += 1
            try:
                send_email('appiispanen@gmail.com','Server has reached '+str(two_hund*50), 'hey Drew,\n Your scraping iteration has gone \n'+str(two_hund*50)+'\n times. Currently on '+condition+'.\n Good luck!')
            except:
                print("############################# E M A I L  F A I L E D. #############################")



######## ONCE EVERYTHING IS COMPLETE, PLEASE GO TO OUTPUT.CSV IN LOCAL DRIVE. HAVE FUN ##########