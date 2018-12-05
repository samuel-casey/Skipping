def edi_table(listy):
    delimiters = ['|','~','-', '*']
    listy = listy.splitlines()
    #  Starts by identifying the delimiter (highest value of the second line of 
    #  the EDI(in case there's an extra line) from the delimiter list)
    #  Reformats the data from EDI to tabled lists (this removes first element too, 
    #  remove "[1:]" to change for normal EDI)
    i= 0
    delim_count ={}
    for delimiter in delimiters:
        delim_count[delimiter]=listy[1].count(delimiter)
    delim, value = sorted(delim_count.items(), key=lambda x: x[1])[-1]
    print('Delimiters in the second line of code: ', delim_count, ' \n Found that the delimiter is --> ', delim)
    for line in listy:
        listy[i] = line.split(delim)
        ##### IF TRADITIONAL EDI WITHOUT SEGMENTED NUMBERS, COMMENT THIS NEXT LINE OUT
        # listy[i]=listy[i][1:]
        i+=1
    if [] in listy:
        listy.remove([])
    return listy
def segment_it(listy):
    st_count=-1
    line_no = 0
    segmented=[]
    segment_include = False
    # return listy
    for line in listy:
        element=line[0]
        if element=='ST' or element=='PO1':
            segment_include=True
            segmented.append([])
            st_count+=1
        if segment_include == True:
            segmented[st_count].append(listy[line_no])
        if element=='SE':
            segment_include=False
        line_no+=1
    return segmented
def find_value(element, code, pos, listy):
    ## Looks through list and returns the value based on the element to look for,
    ## code to look for, and then the number of positions to jump
    for line in listy:
        found_element = line[0]
        found_code = line[1]
        if code == '':
            found_code = code
        if code == found_code and element == found_element:
            value = line[pos]  
    return value 
def LIN_value(element, code, listy):
    value = ''
    for line in listy:
        found_element = line[0] 
        if found_element == element:
            try:
                line.index(code)
                value = (line[line.index(code)+1])
            except:
                continue
    return value
def nocode_lookup(element, listy, pos=1):
    value=''
    for line in listy:
        found_element = line[0]
        if found_element == element:
            value = line[pos]
    return value
def SAC_lookup(element, code, listy):
    value = ''
    for line in listy:
        found_element = line[0] 
        if found_element == element:
            try:
                line.index(code)
                value = (line[line.index(code)+1])
            except:
                continue
    return value
def cond_lookup(element,pos,conditions,listy,concat=[]):
    ### IF YOU GIVE IT A DICTIONARY, IT ASSUMES CONDITIONALS
    ### IF A LIST, IT LOOKS FOR ANY OF THOSE CODES
    value=''
    if isinstance(conditions,dict):
        for line in listy:
            match_count = 0
            found_element = line[0]
            if found_element == element:
                for number in conditions:
                    try:
                        line.index(conditions[number])
                        match_count+=1
                    except:
                        value = ''
                if match_count==len(conditions):
                    value = line[pos]
                    break
            continue
    if isinstance(conditions,list):
        for line in listy:
            found_element = line[0]
            if found_element == element:
                found_code = line[1]
                if found_code in conditions:
                    value = line[pos]
                    break
    if value != '' and concat and concat!=[0,0]:
        value = value[concat[0]:concat[1]]
    return value