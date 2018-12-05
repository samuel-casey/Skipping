def errorhandle(edi):
    error= ''
    if not isinstance(edi, list):
        raise TypeError('Internal Segmenting Error: Data Not List')
        error = '\nInternal Segmenting Error: Data Not List'
    if len(edi)<1:
        print("One segment ")
        error = error + '\nOnly one segment'
    return error

def finalerrors(check, checked, unable):
    if len(check)>0:
        for item in check:
            line = item[-1]

            return '\nITEMS NOT INSERTED IN DAT\nCheck item on line: '+str(line)+' item: '+str(item)+'\nPlease check missing values above'
