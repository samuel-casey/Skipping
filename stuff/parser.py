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
main = listy[i:]

aw_set_purpose=[]

def parse(data):
    counter = []
    i=0
    po_count=0
    delim = "*"
    def splitindex(text, line):
        return line.split.index(text)
    for line in data:
        if 'SE' in line[:10]:
            counter.append(i)
            i+=1
        if 'BQR' in line:
            line = line.split(delim)
            ind=line.index('BQR')
            aw_set_purpose.append(line[ind+1])
        if 'PO1' in line:
            po_count+=1
            


    print(counter)        
    print(
    "H1",aw_set_purpose[0], po_count
    )






parse(main)

