#####   Import the files #####
from a import listy
# print(listy)
listy=listy.splitlines()
# print(listy[1:13])
# print(listy)


###### Break data into two parts - header and listy (main section)  #####
i=0
for line in listy:
    i+=1
    if "GE" in line:
        break

headers = listy[:i]
listy = listy[i:]
# print(headers)
# print(listy)
# find segment numbers
dict1={}
num = []
txt=[]

###### New dictionary breaks apart by segment #####

for line in listy:
    seg_num=line[:5]
    if seg_num not in num and seg_num!='':
        num.append(seg_num)
        dict1[seg_num]=[line[6:]]
    elif seg_num in num and seg_num!='':
        dict1[seg_num].append(line[6:])

# print(num)
record = {}
i=0
# print(dict1)

for line in headers:
    if 'BIA' in line:
        line = line.split("*")
        ind=line.index('BIA')
        Trans_Purpose=line[ind+1]
        Req_ID=line[ind+3]
        Resp_Gen_Date=line[ind+3]
        Resp_Gen_Time=line[ind+4]
    if 'DTM' in line:
        line = line.split("*")
        ind=line.index('DTM')
        Time_Zone=line[ind+6]
        Process_Date=line[ind+7][:8]
        Process_Time=line[ind+7][8:]
    if 'N1' in line:
        line = line.split("*")
        ind=line.index('N1')
        Pipeline_Name=line[ind+4]
        Pipeline_Code=line[ind+4]
    if 'LIN' in line:
        line = line.split("*")
        ind=line.index('LIN')
        Dataset_Request=line[ind+3]
    if 'REF' in line:
        line = line.split("*")
        ind=line.index('REF')
        Reference_Number= line[ind+1]
        Data_Available_Code= line[ind+2]
        
        print(line)

###### Record is the cleaned dictionary of the individual segment dictionaries and their fields #####

for element in dict1:
    record[i]={}
    seg = record[i]
    seg['POS']={}
    pos=0
    for line in dict1[element]:
        if 'DTM*580' in line:
            seg['DTM_580'] = line[:]    
        if 'N1*SJ' in line:
            seg['N1_SJ'] = line[-9:]
        if 'N1*M2' in line:
            seg['N1_M2'] = line[6:]
        if 'N1*MQ' in line:
            seg['N1_MQ'] = line[6:]
        if 'PO1*1' in line:
            if seg['POS']!={}:
                seg['mult_POs'] = True
                seg['POS'][pos]=line[:]
            else:
                seg['POS'][pos] = line[:]
                seg['mult_POs'] = False
            pos+=1
        seg['POS'][pos] = line[:]
    i+=1

##### Testing Samples #####

# print(record)
print()
# print(num)
# for segment in record:
#     if 'N1_M2' in record[segment]:
#         print(str(segment)+"- Receipt: "+record[segment]['N1_M2'])
#     if 'N1_MQ' in record[segment]:
#         print(str(segment)+"- Delivery: "+record[segment]['N1_MQ'])
#     print(record[segment])
print('''

sample flat file (NOT CALIBRATED:)

PO1 for [account] is:     '''+record[3]['POS'][0]+"""




FLAT FILE HEADER
""" )

print(
"RH",Trans_Purpose,Req_ID,Resp_Gen_Date,Resp_Gen_Time,Time_Zone,Process_Date,Process_Time,Pipeline_Name,Pipeline_Code,"\nRD",Dataset_Request,Reference_Number,Data_Available_Code)
# )

