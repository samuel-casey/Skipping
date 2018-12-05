from udf_specs import *
import os
import sys
from lookups import *
import tester
from errorhandle import errorhandle, finalerrors
from copy import copy

error_file = open("C:\\Transfer\\errorrpt.txt", "w")
# UNCOMMENT BELOW FOR CMD SUPPORT
if len(sys.argv) > 1:
     fname = sys.argv[1]
else:
    print('Please enter file name as argument')
    exit()

# # DEFAULT TO EDI.EDI
# fname='C:\Transfer\\trueEDI\W0G23T0B.byp'
# fname='sample1.edi'

print('******            EDI TO UDF CONVERSIONS     ******\nOpening file called '+fname+' ...')
with open(fname) as file:  
        listy1 = file.read()
# udf_award = udf[14:]

listy = edi_table(listy1)

checktable = edi_table(listy1)
i=0
for line in checktable:
    line.append(i)
    i+=1
checkedoff = []
unablelist = []
udf_string = ''
listy = segment_it(listy)
before_errors = errorhandle(listy)
error_file.write('EDI Conversion for: '+fname)
error_file.write(before_errors)

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
indexer=[]
if header!=[]:
    for thing in udf_header:
        # print(segment)
        spec = thing[1]
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
        if len(spec)!=1:
            indexer = [element for element in checktable if spec[1]==element[0]]
            # print('indexer: *******',indexer, value)
            for something in indexer:
                try:
                    something.index(value)
                    checktable.remove(something)
                    checkedoff.append(something)
                    # print(something,' was Removed')
                except:
                    unablelist.append([spec[1], value])
        if thing[0] == m and value == '':
            print('\n***** 846 HEADER ERROR:  *****')
            raise ValueError('*** MANDATORY ELEMENT NOT FOUND-->',spec,udf_string)
            
else:
    raise ValueError('\n\n*********************** ERROR 846 HEADER IS NOT FOUND ********************\n\n')
#### NOW FOR THE REST, BUT WE JUST HAVE TO INITIALIZE THE STUPID IL LINE : 
print("REAL LOOKUP ************")
last_count,n1_count,last_line = 0,0,''
origin = udf_award
for segment in awards:
    n3, n1 = True,True
    # checktable = [item for sublist in segment for item in sublist]
    # print(checktable)
    last_count = n1_count
    if segment[0][0] == 'PO1':
        N1s = [line[0] for line in segment if line[0]=='N1']
        n1_count = N1s.count('N1')
        for i in range(n1_count):
            udf_award.extend(udf_il)
    else:
        n1_count = 0
    for i in range(last_count):
            for item in udf_il:
                udf_award.remove(item)
    il_count = 0
    last_spec1 = ''
    ####  ## NOW THE REAL LOOKUP ## #### 
    ####  ## WHEN IN DOUBT LOOK THROUGH/CITE THE HEADER AGAIN:
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
                        # if spec[1]=='NTE':
                        #     print('NTE at '+spec[2]+value, listy)
            if len(spec) == 7:
                value = value[spec[5]:spec[6]]
            if spec[1]=='NTE' and value!='864':
                values =MSGIT(spec[1], segment, code=spec[2], last_spec = last_spec1)
                value=''.join(values)
                length = spec[3]*len(values)
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
        # LINE CHECKER
        if len(spec)!=1:
            indexer = [element for element in checktable if spec[1]==element[0]]
            # print('indexer: *******',indexer, value)
            for something in indexer:
                try:
                    something.index(value)
                    checktable.remove(something)
                    checkedoff.append(something)
                    # print(something,' was Removed')
                except:
                    unablelist.append([spec[1], value])
        
        #### NOW, LET'S PRINT THE UDF IN UDF_STRING
        if last_line == '\nUL' and value!='' and value!=spec[0]:
            old_val = value
            if '.' not in value:
                value = value+'.'
            up_to_dec = value[:value.index('.')].zfill(4)
            newvalue = value[value.index('.')+1:]
            value = up_to_dec+newvalue+(length-len(up_to_dec)-len(newvalue))*'0'
            # print('Oldval: '+old_val+' NewVal: '+value+' uptodec: '+up_to_dec+' newval: '+newvalue)
        if len(spec)>1 and spec[1]=='SDQ' and value!='':
            value = value.zfill(length)
        udf_string = udf_string+value+' '*(length-len(value))

        if '\n' in spec[0]:
            last_line = spec[0]
        last_spec1 = spec[0]
        



#### SYSTEM NOTICES (STAPLED ONTO THE END) #####
if sys_not!=[]:
    print('(Notice attachments found)')
    for notice in sys_not:
        for spec in sys_not_udf:
            
            if len(spec)>3:
                length = spec[3]
                if spec[2]=='':
                    value = nocode_lookup(spec[1], notice,pos=spec[4])
                if len(spec)==5:
                    try:
                        value = find_value(spec[1],spec[2],spec[4],notice)
                    except:
                        try:
                            value = find_value(spec[1],spec[2],spec[4],header_segment)
                        except:
                            value = ''
                if len(spec)>6:
                    try:
                        value =cond_lookup(spec[1],spec[4],spec[5],notice,0,0)
                    except:
                        try:
                            value =cond_lookup(spec[1],spec[4],spec[5],header_segment,0,0)
                        except:
                            value = ''
            else:
                value = spec[0]
                length = len(spec[0]) 

            if len(spec)==3:
                values = MSGIT(spec[1],notice)
                value, i = '',0
                for result in values:
                    if i>=1:
                        value = value+'\nS4'
                    value =  value+result+' '*(spec[2]-len(result))
                    i+=1
                length = len(value)
            udf_string = udf_string+value
            udf_string = udf_string+' '*(length-len(value))
            # LINE CHECKER
            if len(spec)!=1:
                indexer = [element for element in checktable if spec[1]==element[0]]
                # print('indexer: *******',indexer, value)
                for something in indexer:
                    try:
                        something.index(value)
                        checktable.remove(something)
                        checkedoff.append(something)
                        # print(something,' was Removed')
                    except:
                        unablelist.append([spec[1], value])

            

#### SYSTEM NOTICES (STAPLED ONTO THE END) #####
else:
    print('\n * No 846 notices were found * \n')

## MAKE FINAL ADJUSTMENTS 
i, gates, adjustments, dingle =0, False, False, False
for line in udf_string.splitlines(): 
    newline = line
    adjustments = False
    ## THIS IS THE REDICULOUS REFERENCE NUMBER CHANGES INTO UDF
    if line[:2]=='H1':
        if line[79:81] == 'YR' or line[79:81] == 'YD':
            newline= list(line)
            newline[81] = '1'
            newline = "".join(newline)
    if ',' in line:
        newline = list(line)
        newline[newline.index(',')] = ';'
        newline = "".join(newline)
    ### NOW JUST REMOVING THE NULL LINES :
    if line[2:].replace(' ','') == '' and not adjustments:  
        newline = ''
    splitted = udf_string.splitlines()
    splitted[i] = newline
    udf_string = '\n'.join(splitted)
    i+=1
udf_string = os.linesep.join([s for s in udf_string.splitlines() if s])
print('UDF print attached. Can also be found as the filename "output.udf" in the local drive:\n')
udf_string=udf_string+'\nÿ'
# print(udf_string)

# # # SEND IT TO UDF FILE FORMAT (TAKE AWAY V\TEST) # # #

text_file = open("C:\\Transfer\\output.udf", "w")
text_file.write(udf_string)
text_file.close()
print('\nSent to udf file format \n*********               CONVERSION COMPLETE                  ************')
### FINAL ERROR HANDLING
ignoreheaders = ['GS','GE','ST','SE','ISA','IEA', 'CTT']
erroritems = [element for element in checktable if element[0] not in ignoreheaders]
# print('****************** Check: ',erroritems)
errors = finalerrors(erroritems,checkedoff,unablelist)
error_file.write(errors)
error_file.close()


if len(sys.argv)>2:
    oldfname= sys.argv[2]
    tester.test(udf_string,oldfname)
