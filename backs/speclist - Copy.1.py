from a import listy
delim = '*'
### Header, element, code,  length, relative position (minus 1),
udf =[
    ['RH'],
    ['trans_purpose','BIA','00',2,1],
    ['request_id','BIA','00',30,3],
    ['response_generation_date','BIA','00',6,4],
    ['response_generation_time','BIA','00',8,5],
    ['HT'],
    ['process_date','DTM','009',14,7],
    ['process_time','DTM','009',14,7],
    ['pipeline_name','N1','SJ',35,4],
    ['pipeline_code','N1','SJ',17,4],
    ['\nRD'],
    ['dataset_request','LIN','',30,3],
    ['reference_number','REF','',2,1],
    ['data_available_code','REF','',30,2],
    ['\nH1'],
    ['aw_set_purpose','BQR','',2,1],
    ['aw_offer_number','BQR','',45,2],
    ['aw_bid_number','REF','BD',30,2],
    ['aw_bid_number','REF','H5',30,2],
    [''*15],
    ['aw_bid_number','REF','',30,2],
]
def edi_table(listy, delim):
    listy = listy.splitlines()
    # Reformats the data from EDI to tabled lists (this removes first element too, 
    # remove "[1:]" to change for normal EDI)
    i=0
    for line in listy:
        listy[i] = line.split(delim)
        listy[i]=listy[i][1:]
        i+=1
    listy.remove([])
    return listy

def segment_it(listy):
    st_count=-1
    line_no = 0
    segmented=[]
    segment_include = False
    # return listy
    for line in listy:
        if line[0]=='ST':
            segment_include=True
            segmented.append([])
            st_count+=1
        if segment_include == True:
            segmented[st_count].append(listy[line_no])
        if line[0]=='SE':
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

def make_udf(udf):
    udf_string = ''
    for element in udf:
        spaces = udf[element][1]
        value = udf[element][2]
        udf_string = udf_string+value
        udf_string = udf_string+(' '*(spaces-len(value)))
    return udf_string

listy = edi_table(listy, delim)

print(segment_it(listy))
udf_string = ''
for spec in udf:
    if len(spec)>1:
        try:
            value = find_value(spec[1],spec[2],spec[4],listy)
            length = spec[3]
        except:
            value = ''
            length = spec[3]
    else:
        value = spec[0]
        length = len(spec[0]) 
    udf_string = udf_string+value
    udf_string = udf_string+' '*(length-len(value))
    print(value)
print('\n'+udf_string)



# print(segment_it(listy))
# print(make_udf(udf))
# print(find_value('GS','IB',3,listy))