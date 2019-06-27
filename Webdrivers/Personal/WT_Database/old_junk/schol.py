import scholarly

# def get_conditions_list(location = "conditions.csv"):
#     with open(location, newline='') as csvfile:
#         condition_reader = csv.reader(csvfile)
#         condition_list = [row[0].lower() for row in condition_reader]
#     return condition_list
# for condition in get_conditions_list():
#     for word in ['food and drinks', 'supplements', 'alternative therapies']
#     search_query = scholarly.search_pubs_query(word+' for '+condition)
condition = 'breast cancer'
search_query = scholarly.search_pubs_query('Treatments for '+condition)


for i in range(1):
    try:
        for query in search_query:
            print(query)
    except:
        print('NONE')
