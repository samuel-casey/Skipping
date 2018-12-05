

from udf_specs import *
import os
import sys
from lookups import *

# UNCOMMENT BELOW FOR CMD SUPPORT
# if len(sys.argv) > 1:
#      fname = sys.argv[1]
# else:
#     print('Please enter file name as argument')
#     exit()

# DEFAULT TO EDI.EDI
fname='sample5.byp'

print('******            EDI TO UDF CONVERSIONS     ******\nOpening file called '+fname+' ...')
with open(fname) as file:  
        listy = file.read()
# udf_award = udf[14:]

listy = edi_table(listy)
udf_string = ''
listy = segment_it(listy)

header, offers,bids,awards,widthdraws,OA,sys_not,rel_cap,IT,FT = ([],[],[],[],[],[],[],[],[],[])
for segment in listy:
    opener = segment[0][0]
    identifier = segment[0][1]
    conditional = segment[1][1]
    if identifier == "846":
        header.append(segment)
        header_segment = header[0]
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
    if opener == 'PO1':
        awards.append(segment)

print('Using file "udf_specs.py" for translation assitance')
##HEADER ONLY (IF AVAILABLE), LOOKS AT FIRST SEGMENT
if header!=[]:
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
else:
    print('\n\n*********************** ERROR 846 HEADER IS NOT FOUND ********************\n\n')
#### NOW FOR THE REST, WHEN IN DOUBT LOOK THROUGH/CITE THE HEADER AGAIN:
last_count = 0
n1_count = 0
origin = udf_award
for segment in awards:
    last_count = n1_count
    if segment[0][0] == 'PO1':
        print('is PO')
        N1s = [line[0] for line in segment if line[0]=='N1']
        n1_count = N1s.count('N1')
        for i in range(n1_count):
            # print(last_count)
            udf_award.extend(udf_il)
    else:
        print('not PO')
        n1_count = 0
    for i in range(last_count):
            for item in udf_il:
                udf_award.remove(item)
    il_count = 0
    print(len(udf_award), n1_count, last_count)
    for spec in udf_award:
        if spec[0]=='\nIL' and n1_count>0:
            il_count+=1
        if len(spec)==5 or len(spec)==7:
            length = spec[3]
            try:
                value = find_value(spec[1],spec[2],spec[4],segment)
            except:
                if segment[0][0]=='PO1':
                    value = ''
                else:    
                    try:
                        value = find_value(spec[1],spec[2],spec[4],header_segment)
                    except:
                        value = ''
            if len(spec) == 7:
                value = value[spec[5]:spec[6]]
        elif len(spec) == 4:
            length=spec[3]
            value = nocode_lookup(spec[1],segment)
        elif len(spec) == 6:
            length = spec[3]
            value = LIN_value(spec[1],spec[2],segment)
        elif len(spec)>7:
            length =spec[3]
            try:
                unit_number = spec[8]
            except:
                unit_number = 0
            value = cond_lookup(spec[1],spec[4],spec[5], segment,[spec[6],spec[7]],unit_number)        
        else: ### IF SPEC EQUALS 1 OR SOMETHING WEIRD, JUST PRINT THE FIRST ITEM.
            value = spec[0]
            length = len(spec[0])  
        # BECAUSE THE IL LINE WAS MADE TO MAKE HUMANITY HATE ITSELF:
        if il_count>0 and len(spec)>1:
            length = spec[3]
            value = il_lookup(spec[1], spec[4],spec[5],segment,count=il_count)
        #### NOW, LET'S PRINT THE UDF IN UDF_STRING
        udf_string = udf_string+value+' '*(length-len(value))
## MAKE FINAL ADJUSTMENTS 
for line in udf_string.splitlines(): 
    ## THIS IS THE REDICULOUS REFERENCE NUMBER CHANGE INTO UDF
    if line[:2]=='H1':
        if line[79:81] == 'YR' or line[79:81] == 'YD':
            newline= list(line)
            newline[81] = '1'
            newline = "".join(newline)
            udf_string=udf_string.replace(line,newline)     
    ### NOW JUST REMOVING THE NULL LINES :
    if line[2:].replace(' ','') == '':  
       udf_string=udf_string.replace(line,'')
udf_string = os.linesep.join([s for s in udf_string.splitlines() if s])
# print('UDF print attached. Can also be found as the filename "output.udf" in the local drive:\n')
# print(udf_string)

# # # SEND IT TO UDF FILE FORMAT (TAKE AWAY V\TEST) # # #

text_file = open("C:\Transfer\output.udf", "w")
text_file.write(udf_string)
text_file.close()
print('\nSent to udf file format \n*********               CONVERSION COMPLETE                  ************')
