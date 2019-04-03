import os

os.chdir('c:\\Transfer\\Scraper')
with open('sender.txt', 'w') as file:
    file.write('TITLE RESCRAPER - THE AFTERNOON CHECKER')

def append(line):
    os.chdir('c:\\Transfer\\Scraper')
    with open('sender.txt', 'a') as file:
        file.write('/n'+line)

with open ('c:\\Transfer\\Scraper\\output2.txt', 'r') as output:
    output_reader = output.read().splitlines()
with open('c:\\Transfer\\Scraper\\macros.txt', 'r') as macro:
    macro_reader = macro.read().splitlines()
    
macro_dirs = [line for line in macro_reader if 'ondownload folder=v:' in line.lower()]
for line in macro_dirs:
    line1 = line.replace('ONDOWNLOAD FOLDER=','').lower()
    try:
        line2 = line1[:line1.index(' file')]
    except:
        print('something was wrong with ',line1)
        raise EOFError
    print(line2)
# for line in reader:
    # for directory in output_reader:
    #     try:
    #         indexer = macro_reader.index(directory)
    #         print(indexer)
    #     except:
    #         print('No directory found for '+directory)
        
# print(macro_dirs)


# append(" (\"C:\Program Files (x86)\\iOpus\\iMacros\\iMacros.Sidebar.exe\" -macro \"C:\\Users\\sbrodeur\\Desktop\\Macros\\"+filename+"\"\n)\nPING localhost -n 2 >NUL\n")