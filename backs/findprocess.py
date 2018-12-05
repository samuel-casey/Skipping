from a import listy
# Specs contain elements which contains a dict of codes which then contain meanings (lists with the meaning term and how many terms past the initial delimiter to find it)
specs= {
    'DTM' : {'050':['Received',7], '580':['Actual_Release',7],'009':['Process_Time',7],'103':['Award_Date',7],'145':['Opening_Date',0],'448':['Occurence_Span',7],'00':['ignore',0]
}, 
    'CTT' : {'*':['PO_span',1],
},
    'REF' : {'RE':['unknown',2], 'IB':['Inbound',2], 'BD':['Bid_No',2], 'IF':['Issue_No',2], 'H6':['unknown', 2], 'ZZ':['Mutually_defined',2], 'H5':['Recall', 2], '99':['Rate Conf. ID', 2],'SV':['Service_Charge_No', 2]

},
    'ST' : {'846':['Header_Segment', 0],'843':['Award_Segment', 0], '864':['Sys_notice',0]
},
    'SE' : {'*':['Segment_Span',1]

},
    'GS' : {'IB':['Award_Header',1]

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
            meaning = specs[element]['*']
        value = line[ind+meaning[1]]
        term = meaning[0]
        print('Element: '+element+', code: '+code+', term: '+term+', value: '+value)
# print(listy)