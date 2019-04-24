import sys
import os
if len(sys.argv) > 1:
     txt = sys.argv[1]
else:
    print('Please enter file name as argument')
    exit()
main_dir = txt[:txt.rfind('\\')]
with open(txt) as file:  
        txt = file.read()

txt = txt.splitlines()


def append(line, txt):
    with open(txt, 'a') as file:
        file.write(line)

newfile = ''
i=0
for line in txt:
    if line[:4] == "grep" or line[:4] == "File" or line[:4] == "Erro" or (line[:4]=="Cycl" and i!=0):
        newline=""
    else:
        newline = line
        append(newline+'\n', main_dir+'\\output.txt')
    i+=1
