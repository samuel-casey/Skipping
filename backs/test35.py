from a import listy
# Specs contain elements which contains a dict of codes which then contain meanings (lists with the meaning term and how many terms past the initial delimiter to find it)
specs= {
    'DTM' : {'009':{7:'Process_Time', 4:'Timezone'},
}, 
        }
        # 'BIA' : {''},}
listy = listy.splitlines()
i=0
for line in listy:
    listy[i]=line[6:]
    i+=1
delim='*'
for line in listy:
    element = line[:3]
    if delim in element:
        element = line[:2]
    line = line.split(delim)
    if element in specs:
        ind=line.index(element)
        code = line[ind+1]
        try:
            specs[element][code]
            meaning = specs[element][code]
        except:
            meaning = 'x'
            # meaning = specs[element]['*']
        print(meaning)

# print(listy)