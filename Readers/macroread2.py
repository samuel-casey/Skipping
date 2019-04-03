import os

def append(line):
    with open('V:\\Test\\output.bat', 'a') as file:
        file.write(line)

# write title of batch file
append('TITLE PROBLEM CHECKER - THINGS DS4 DOESN\'T DO\n:START\n')

#Now look through each Macro:
for filename in os.listdir('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros'):
    with open('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros\\'+filename, 'r') as file:
        reader = file.read().lower()
        # print(reader)
    v_ind, type_ind, macro_directory = 0,0,''
    #Found the macro, now read the lines:
    for line in reader.splitlines():
        try:
            # Let's look for a "V" drive present (Where the macros typically look): 
            v_ind = line.index("v:\\")
            file_ind = line.index(" file")
            macro_directory = line[v_ind:file_ind]
            break
            # If we don't find one, we just move along.
        except:
            continue
    # Now, let's look through the ds4 batch file to figure out if we can find a script directory that matches our search directory:
    with open('C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\ds4.bat', 'r') as files:
        readers = files.read().lower().splitlines()
    try:
        # We'll take the found directory from the 4th position so that we get after the V:\\
        ds4_dir = [line for line in readers if macro_directory in line][0][4:]
        # Go up until the * to get everything until the last \ : 
        ext = ds4_dir[ds4_dir.index("*"):]
        print("DS4 " + ds4_dir +" And Macros dir: " + macro_directory+ " " +ext)
        # Write the code in the batch - Run the macro if the file ds4 searches does not exist:
        append('\n\nIF NOT EXIST '+ds4_dir+ " (\"C:\Program Files (x86)\\iOpus\\iMacros\\iMacros.Sidebar.exe\" -macro \"C:\\Users\\sbrodeur\\Desktop\\Macros\\"+filename+"\"\n)\nPING localhost -n 2 >NUL\n")
        # Error report - send an errorrpt.txt to the dir saying the file does not work (for nothing was pulled).
        append('IF NOT EXIST '+ds4_dir+" echo %DATE% "+filename+" DOES NOT WORK >> errorrpt.txt")
    except:
        continue
append('\n@pause')
       
        