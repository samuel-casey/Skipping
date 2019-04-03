import os, glob, datetime
os.chdir('c:\\Transfer\\Scraper')
with open('output2.txt', 'w') as file:
    file.write('')
def append(line):
    os.chdir('c:\\Transfer\\Scraper')
    with open('output2.txt', 'a') as file:
        file.write(line+'\n')
os.chdir('c:\\Users\\apiispanen\\Desktop\\pyscripts\\Readers')
# READ THE OUTPUT OF SPECIFICATIONS (IE WHAT FILES TO LOOK FOR IN EACH DIRECTORY AND HOW MANY)
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
        try:
            unix_date = os.path.getmtime(directory+'\\'+files_of_interest[0])
            date = datetime.date.fromtimestamp(unix_date)
            today = datetime.date.today()
            are_files_recent = date == today
        except:
            are_files_recent= True
        is_match = len(files_of_interest) >= int(num_files[0])
        if not is_match or not are_files_recent:
            print(directory+' how many '+f_type+' files found - '+str(len(files_of_interest))+' needed - '+str(num_files[0]), date)
            append(directory)
