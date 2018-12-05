from a import listy
# print(listy)
listy=listy.splitlines()
delim='*'
for line in listy:
    if 'DTM'+delim+'009' in line:
        print(line[-14:])
    