from a import listy
import os
delim = '*'
### Header, element, code,  length, relative position (minus 1), 
### (OPTIONAL: Concat pos start, and concat pos end)
udf =[ ### HEADER
    ['RH'],
    ['trans_purpose','BIA','00',2,1],
    ['request_id','BIA','00',30,3],
    ['response_generation_date','BIA','00',6,4],
    ['response_generation_time','BIA','00',8,5],
    ['HT'],
    ['process_date','DTM','009',14,7,0,8],
    ['process_time','DTM','009',14,7,8,14],
    ['pipeline_name','N1','SJ',35,4],
    ['pipeline_code','N1','SJ',17,4],
    ['\nRD'],
    ['dataset_request','LIN','',30,3],
    ['reference_number','REF','',2,1],
    ['data_available_code','REF','',30,2],
    ### END OF HEADER
    ### AWARD
    ['\nH1'],
    ['aw_set_purpose','BQR','',2,1],
    ['aw_offer_number','BQR','',45,2],
    ['aw_bid_number','REF','BD',30,2],
    ['reference_number','REF','H5',30,2],
    [''*15],
    [''*2], 
    ['transaction_date','DTM','009',35,7],
    ['request_id','BIA','',30,3],
    [''*15],
    ['re_releasable_ind','REF','H6',1,2],
    ['award_number','REF','IF',30,2],
    ['\nN1'],
    ['special_terms_text','NTE','GEN',350,2],
    ['\nN2'],
    ['qty_text_description', 'NTE', 'QUT', 350,2],
    ['\nN3'],
    ['recall_terms','NTE', 'ZZZ', 350, 2],
    ['\nH2'],
    ['aw_tm_zone','DTM','050',2,4],
    ['capacity_aw_dt','DTM','050',14,7,0,8],
    ['capacity_aw_tm','DTM','050',14,7,8,14],
    ['aw_post_dt','DTM','103',14,7],
    ['aw_post_tm','DTM','103',14,7],
    ['aw_beg_dt','DTM','580',35,7],
    ['aw_beg_tm','DTM','580',35,7],
    ['aw_end_dt','DTM','580',35,7],
    ['aw_end_tm','DTM','580',35,7],

    ['']
    
]
udf_header = udf[:14]
udf_award = udf[14:]

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
        element=line[0]
        if element== 'PO1':
            segmented.append([])
            st_count+=1
        if element=='ST':
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
def make_udf(udf):
    udf_string = ''
    for element in udf:
        spaces = udf[element][1]
        value = udf[element][2]
        udf_string = udf_string+value
        udf_string = udf_string+(' '*(spaces-len(value)))
    return udf_string

listy = edi_table(listy, delim)
# print(segment_it(listy))
# print(listy)
udf_string = ''
listy = segment_it(listy)

##HEADER ONLY, LOOKS AT FIRST SEGMENT
header, offers,bids,awards,widthdraws,OA,sys_not,rel_cap,IT,FT = ([],[],[],[],[],[],[],[],[],[])
for segment in listy:
    identifier = segment[0][1]
    conditional = segment[1][1]
    if identifier == "846":
        header.append(segment)
    if identifier == "840":
        offers.append(segment)
    if identifier == "843":
        if conditional == "15" or conditional == "06":
            awards.append(segment)
        if conditional == "BI" or conditional == "BW":
            bids.append(segment)
        if conditional == "B":
            widthdraws.append(segment)
    if identifier == "873":
        OA.append(segment)
    if identifier == "864":
        sys_not.append(segment)
# print(sys_not)
# print(awards)
# segment = listy[0] with
header_segment = header[0]
# print(header_segment)
for spec in udf_header:
    # print(segment)
    if len(spec)>1:
        try:
            value = find_value(spec[1],spec[2],spec[4],header_segment)
        except:
            value = ''
        length = spec[3]
    else:
        value = spec[0]
        length = len(spec[0]) 
    if len(spec)>5:
            # print(value)
            value = value[spec[5]:spec[6]]
    udf_string = udf_string+value
    udf_string = udf_string+' '*(length-len(value))

#### NOW FOR THE REST, WHEN IN DOUBT LOOK THROUGH/CITE THE HEADER AGAIN:
for segment in listy[1:]:
    for spec in udf_award:
        if len(spec)>1:
            try:
                value = find_value(spec[1],spec[2],spec[4],segment)
            except:
                try:
                    value = find_value(spec[1],spec[2],spec[4],header_segment)
                except:
                    value = ''
            length = spec[3]
        else:
            value = spec[0]
            length = len(spec[0]) 
        if len(spec)>5:
            # print(value)
            value = value[spec[5]:spec[6]]
        udf_string = udf_string+value+' '*(length-len(value))
# print(udf_string)

## REMOVE NULL LINES
for line in udf_string.splitlines(): 
    if line[2:].replace(' ','') == '':  
       udf_string=udf_string.replace(line,'')
udf_string = os.linesep.join([s for s in udf_string.splitlines() if s])

print(udf_string)

text_file = open("Output.txt", "w")
text_file.write(udf_string)
text_file.close()

# print(udf_string)
#     print(value)
# print('\n'+udf_string)



# print(segment_it(listy))
# print(make_udf(udf))
# print(find_value('GS','IB',3,listy))