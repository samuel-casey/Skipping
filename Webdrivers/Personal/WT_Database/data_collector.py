import relationdrive, define

def open_and_run(conditions_list_location = 'conditions.csv', treatment_list_location = 'treatments.csv', output_location = "output.csv" ):
    # define.clear_file()  #  IF YOU'D LIKE TO CLEAR THE OUTPUT FILE 
    
    ## STEP 1 - Define the variables needed ###
    treatment_categories = ['Food and Drinks','Supplements', 'Alternative Therapies']
    
    #### STEP 2  - Get Conditions ####
    condition_list = define.get_conditions_list(conditions_list_location)[1:100]
    '''First stage - Up to 100 - Ran on 5-21-2019''' 
    
    #### STEP 3 - Iterate over Condition and Category
    for condition in condition_list:
        for Category in treatment_categories:
            url, score, matched_treatments = relationdrive.list_text(relationdrive.driver, condition, Category)
            define.enter_record(matched_treatments, condition, Category, score, url)

if __name__ == "__main__":
    open_and_run()