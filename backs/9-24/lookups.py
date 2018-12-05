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
    # value=''
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
def nocode_lookup(element, listy, pos=1, skip=-1):
    value=''
    if skip>-1:
        try:
            value = [line for line in listy if element==line[0]][skip][pos]
            return value
        except:
            pass
    else:
        for line in listy:
            found_element = line[0]
            if found_element == element:
                value = line[pos]
    return value
def SAC_lookup(element, code, listy):
    ### Finds the value by searching for the code within the line of the found element.
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
def cond_lookup(element,pos,conditions,listy,concat,unit_number):
    ### IF YOU GIVE IT A DICTIONARY, IT ASSUMES CONDITIONALS
    ### IF A LIST, IT LOOKS FOR ANY OF THOSE CODES
    value=''

    #
    if isinstance(conditions,dict): #and not isinstance(list(conditions.values())[0], list):
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

    # CONDITIONAL LIST MEANS 
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
def il_lookup(element, pos,conditions, listy, count=0):
    # print(element)
    value = ''
    count = count-1
    if element == 'PO1':
        line = [line for line in listy if line[0]==element][0]
        seg_line = line[::2]
        value = line[(seg_line.index('MO')*2)+1]
        return value
    elif isinstance(conditions,int):
        try:
            value = [line for line in listy if line[0]==element][count][pos]
        except:
            value=''
    else:
        try:
            target_line = [line for line in listy if line[0] == element][count]
        except:
            target_line = []
        match_count =0
        #DELETE
        for number in conditions:    
            for unit in conditions[number]:
                try:
                    target_line.index(unit)
                    match_count+=1
                except:
                    value = ''
        if match_count==len(conditions):
            value = target_line[pos]
         
        #DELETE
        # for cond in conditions:
        #     if target_line[cond] in conditions[cond]:
        #         value = target_line[pos]
    return value    
def MSGIT(element, notice, code=None, last_spec=None, skip=0):
    values=[]
    if element =='NTE':
        messages = [line for line in notice if line[0]==element and line[1]==code]
        if len(messages)>0:
            for message in messages:
                    values.append(last_spec+message[2])
        else:

            ###DELETE DELETE
            if values==[] and element=='NTE' and code=='ZZZ':
                bqr = [line for line in notice if len(line)>3 and (line[0], line[1], line[3])==('REF','H5','864')]
                try:
                    values = [last_spec+bqr[0][3]]
                except:
                    pass
            elif values==[] and element=='NTE' and code=='GEN':
                bqr = [line for line in notice if len(line)>3 and (line[0], line[1], line[3])==('REF','L1','864')]
                try:
                    values = [last_spec+bqr[0][3]]
                except:
                    pass
            ###DELETE DELETE

            else:
                values = [last_spec]
            # print(element, code, 'NOTHING FOUND', values, notice)
    else:
        messages = [line for line in notice if line[0]==element]
        # print(messages, skip)
        if element == 'MSG':
            values = [line[1] for line in messages]
            returned = []
            for value in values:
                returned.append('\nS4'+value)
            values = ''.join(returned)
        else: 
            try:
                values = messages[skip][1]
            except:
                values = []
        # for message in messages:
        #     values.append(message[1])
        # print(notice, message)
        # print(messages, skip, values)
    return values

