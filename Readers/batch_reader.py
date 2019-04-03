import os
batch_directory = 'C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\MACRO_BAT'
directory = os.listdir(batch_directory)
os.chdir(batch_directory)
def append(line):
    with open(batch_directory+'\\output.txt', 'a') as file:
        file.write(line)
for batch_name in directory:
    with open(batch_name, 'r') as batch:
        batch_read = batch.read().splitlines()
    for line in batch_read:
        if 'Program Files' in line:
            append(line+'\n')