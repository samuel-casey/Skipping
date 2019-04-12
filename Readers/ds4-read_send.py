import os
import datetime
batch_dir = 'C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros'
real_batch_dir = 'C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\MACRO_BAT'
read_dir = 'c:\\Users\\apiispanen\\Desktop\\pyscripts\\Readers\\'
os.chdir('c:\\Transfer\\Scraper')
with open('c:\\Transfer\\Scraper\\sender.bat', 'w') as file:
    file.write('TITLE RESCRAPER - THE AFTERNOON CHECKER '+str(datetime.date.today()))


def append_line(line):
    os.chdir('c:\\Transfer\\Scraper')
    with open('sender.bat', 'a') as file:
        file.write('\n'+line)

with open ('c:\\Transfer\\Scraper\\output2.txt', 'r') as output:
    output_reader = output.read().splitlines()
with open('c:\\Transfer\\Scraper\\macros.txt', 'r') as macro:
    macro_reader = macro.read().splitlines()


#MAKE LIST OF the ONDOWNLOAD lines of macros (and lowercase them)    
# macro_dirs = [line for line in macro_reader if 'ondownload folder=v:' in line.lower()]

os.chdir(batch_dir)
macro_dirs, intended_macros = {}, []

for batch in os.listdir(batch_dir):
    with open(batch,'r') as batch_read:
        batch_reader = batch_read.read().splitlines()
    for line in batch_reader:
        # print(line)
        if 'ondownload folder=v:' in line.lower():
            line1=line.lower()
            try:
                line2 = line1[:line1.index(' file')].replace('ondownload folder=','')
            except:
                line2 = line
            if line2 not in macro_dirs:
                macro_dirs[line2] = batch
        elif 'saveas type=extract folder=v' in line.lower():
            line1=line.lower()
            try:
                line2 = line1[:line1.index(' file')].replace('saveas type=extract folder=','')
            except:
                line2 = line
            if line2 not in macro_dirs:
                macro_dirs[line2] = batch
for line in output_reader:
    try:
        intended_macros.append(macro_dirs[line])
    except:
        print('No macro found for ', line)
intended_macros.sort()
print(intended_macros)
lines_made = []

### COMMENT OUT BELOW FOR REFORMATTING FOR MY COMP ###

# for macro_name in intended_macros:
#     for batch_name in os.listdir(real_batch_dir):
#         with open(real_batch_dir+'\\'+batch_name, 'r') as mb:
#             macro_bat = mb.read().splitlines()
#         for line in macro_bat:
#             if (macro_name in line) and (line not in lines_made):
#                 lines_made.append(line)
#                 append_line(line)
#                 break

###### REFORMATTER (IF U WANT) ##########

for macro_name in intended_macros:
    for batch_name in os.listdir(real_batch_dir):
        with open(real_batch_dir+'\\'+batch_name, 'r') as mb:
            macro_bat = mb.read().splitlines()
        for line in macro_bat:
            if (macro_name in line) and (line not in lines_made):
                lines_made.append(line)
                try:
                    line = line.replace('x86\\iMacros.exe', 'iMacros.Sidebar.exe')
                except:
                    continue
                append_line(line)
                break


########### END COMMENTING OUT ##########
print(lines_made)
