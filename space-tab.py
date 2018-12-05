import sys
if len(sys.argv) > 1:
     txt = sys.argv[1]
else:
    print('Please enter file name as argument')
    exit()
with open(txt) as file:  
        txt = file.read()

txt = txt.splitlines()


def append(line, txt):
    with open(txt, 'a') as file:
        file.write(line)

newfile = ''
for line in txt:
    if '   ' in line:
        line = line.split(' ')
        last_seg = ''
        newline = ''
        seg_counter = 0
        for seg in line:
            if seg == '':
                seg_counter+=1
                if last_seg!='' or seg_counter>9:
                    newline= newline+'\t'
                    if seg_counter >9:
                        seg_counter = 0
            else:
                seg_counter=0
                if last_seg == '':
                    newline = newline+seg    
                else:
                    newline = newline+' '+seg
            last_seg = seg
        newline = ''.join(newline)
    else:
        newline = line
    append(newline+'\n','output.txt')

