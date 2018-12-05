import os
# for root, dirs, files in os.walk(, topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
        
#     for name in dirs:
#         print(os.path.join(root, name))
print('START')
def append(line):
    with open('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros\\output.txt', 'a') as file:
        file.write(line)
append('TITLE PROBLEM CHECKER - THINGS DS4 DOESN\'T DO\n:START\n')

for filename in os.listdir('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros'):
   
    with open('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros\\'+filename) as reader:
            macro = reader.read()
    macro = macro.splitlines()
    try:
        open('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\MACRO_BAT\\'+filename[:filename.index('.')]+'.bat')
        try:
            dir_line = [line for line in macro if 'V:\\' in line][0]
            append('IF NOT EXIST ')
            directory = dir_line[dir_line.index('V:\\'):dir_line.index('FILE')-1]
            print(directory)
            with open('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\ds4.bat') as bat:
                batch = bat.read().lower()
            try:
                tmp = batch.index(directory.lower())
                endindex = tmp+batch[tmp:].index('\n')
                ds4_dir = batch[tmp:endindex]
                print("FOUND ONE!!!! ****", ds4_dir)
            except:
                print('no DS4 found')
            append(ds4_dir)
            append(' ')
            try:
                append(filename[:filename.index('.')]+'\n')
            except:
                append('Start'+'\n')
        except:
            print('No dir found for '+filename)
    except:
        print('NO BAT FOR ', filename)
append('goto START\n\n')

# NOW FOR THE FUNCTIONS
for filename in os.listdir('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros'):
    root = filename[:filename.index('.')]
    try:
        with open('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\MACRO_BAT\\'+root+'.bat') as reader:
            macro_bat = reader.read()
        append('\n\n:')
        try:
            append(root)
        except:
            append(filename)
        append('\n')
        append(macro_bat)
        append('\ngoto START')
    except:
        print(root + 'root cannot be found, help')

append('goto START')
    with open(filename) as file:
        file = file.read()
with open('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros\\output.txt') as file:
        output = file.read()


