import os
import glob
# Reads the ds4 batch file to determine what macros have what specs:
def ds4_read():
    def append(line):
        with open('output.txt', 'a') as file:
            file.write(line)
    # Set Working Directory
    os.chdir('c:\\Users\\apiispanen\\Desktop\\pyscripts\\Readers')
    #Now look through DS4:
    with open('DS4.bat', 'r') as file:
            reader = file.read().lower()
    append('[Directory],[File Type],[Number of files (list too)],[Code [0std, 1between, 2<,3>]]')
    for line in reader.splitlines():
        if line[:3] == "dir":
            full_line = line[4:]
            f_type = full_line[full_line.rfind('\\'):]
            prev_dir = full_line[:full_line.rfind('\\')]
            print(prev_dir,f_type,full_line)
            # if dir, print path.
        if 'should be' in line:
            should_num = line[line.index('should be')+9:]
            real_num = [int(s) for s in should_num.split() if s.isdigit()]
            append("\n["+str(prev_dir)+"],["+f_type+']')
            if 'at least' in line:
                append(","+str(real_num)+',[2]')
            if len(real_num)==2:
                append(','+str(real_num)+',[1]')
            else:
                append(','+str(real_num)+',[0]')
# Read the directories in ops to find files and compare w/specs:
def ds4_read2():
    os.chdir('c:\\Transfer\\Scraper')
    with open('output2.txt', 'w') as file:
        file.write('')
    def append(line):
        os.chdir('c:\\Transfer\\Scraper')
        with open('output2.txt', 'a') as file:
            file.write(line+'\n')
    os.chdir('c:\\Users\\apiispanen\\Desktop\\pyscripts\\Readers')
    with open('output.txt', 'r') as file:
            reader = file.read().lower().splitlines()
    print('Reading ',len(reader),' directories for matches')
    for i in range(1,len(reader)):
    # for i in range(1,25): #FOR TESTING
        list_item = reader[i].split('],[')
        directory,f_type,num_files,code = list_item[0].replace('[',''),list_item[1][1:],list_item[2],list_item[3].replace(']','')
        num_files = num_files.split(',')
        # print(directory,f_type,num_files)
        if 'f:\\' not in directory: 
            os.chdir(directory)
            files_of_interest = [f for f in glob.glob(f_type)]
            is_match = len(files_of_interest) >= int(num_files[0])
            if not is_match:
                print(directory+' how many '+f_type+' files found - '+str(len(files_of_interest))+' needed - '+str(num_files[0]))
                # append(directory+' how many '+f_type+' files found - '+str(len(files_of_interest))+' needed - '+str(num_files[0])
                append(directory)
# Reads all macros to determine what directory pertained to what macro:
def macro_reader(test_dir, directory_of_macros):
    # import glob
    print('TEST DIR ',test_dir,' MACROS IN ',directory_of_macros)
    import os    
    os.chdir(directory_of_macros)
    files_of_interest = os.listdir(directory_of_macros)
    for file in files_of_interest:
        with open(file, 'r') as macro:
            script = macro.read().splitlines()
        dirs_found = [line for line in script if test_dir in line.lower()]
        try:
            return [file,dirs_found[0]]
        except:
            continue


# Takes a test directory and returns all elements found in the directory of macros (or any filetype)


dir = 'C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macros'
test_dir = 'V:\\Gas_Qual\\West\\WBI'
macros_needed = []
with open('c:\\Transfer\\Scraper\\output2.txt','r') as file:
    reader = file.read().splitlines()
    for line in reader:
        edited_line = line.replace('\\','\\\\').lower()
        try:
            macros_needed.append(macro_reader(line,dir)[0]) 
        except:
            print('No match for ', edited_line)
print(macros_needed)
# print(macro_reader(test_dir,dir))  
