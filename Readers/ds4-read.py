import os

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
        