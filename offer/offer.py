from off_specs import *
from offer_lookup import *
# with open('listy') as listy:
#     listy = listy.read()
listy = edi
listy = make_table(listy)
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
print('headers:',len(header),'offers: ',len(offers),'bids: ',len(bids),'Notices: ',len(sys_not))
udf_string = ''
for spec in headerspec:
    value = find_value(spec, header_segment)
    print(value)
    udf_string = udf_string+value

print(udf_string)

