with open('edi.edi') as edi:
    listy = edi.read()
listy = listy.splitlines()
#    THIS JUST TAKES AN EDI WITH LOOP NUMBERS AND CONVERTS IT BACK TO NORMAL!!
i= 0
delim_count ={}
delim = "*"
for line in listy:
    listy[i] = line.split(delim)
    ##### IF TRADITIONAL EDI WITHOUT SEGMENTED NUMBERS, COMMENT THIS NEXT LINE OUT
    listy[i]=listy[i][1:]
    i+=1
if [] in listy:
    listy.remove([])
count=0
for line in listy:
    listy[count] = '*'.join(line)
    count+=1
count2=0
listy = '\n'.join(listy)
text_file = open("sample1.edi", "w")
text_file.write(listy)
text_file.close()
