def DS4_pref(ds4_path):
    directory, num_of_files, f_type, find_type, prev_dir, should_num = '','','','','',0

    with open(ds4_path, 'r') as file:
        reader = file.read().lower()
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
            if 'at least' in line:
                find_type= 2
            if len(real_num) == 2:
                find_type = 1
            else:
                find_type = 0
        return [prev_dir, should_num, f_type, find_type]

print(DS4_pref('c:\\Users\\apiispanen\\Desktop\\pyscripts\\Readers\\ds4.bat'))