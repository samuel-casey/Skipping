import os

def append(line):
    with open('V:\\Test\\output.txt', 'a') as file:
        file.write(line)

macro_dir = 'C:\\Users\\apiispanen\\Desktop\\SCRIPTS\\Macro_BAT'

for filename in os.listdir(macro_dir):
    with open(macro_dir+'\\'+filename, 'r') as file:
        reader = file.read().lower()
        if "-loop" in reader:
            append(reader)