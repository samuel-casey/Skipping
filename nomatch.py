# import ediudf
import glob
import os
for filename in glob.glob('C:\Transfer\EDI\*.byp'):
   
    datfile = ''
    file = filename.split('\\')[-1]
    root = file[:-3]
    print(root)
    datfile = root+'DAT'
    if os.path.isfile('C:\Transfer\DAT\\'+datfile):
        datfilename = 'C:\Transfer\DAT\\'+datfile
        os.rename('C:\Transfer\DAT\\'+datfile,'C:\Transfer\TrueDAT\\'+datfile)
        os.rename(filename,'C:\Transfer\TrueEDI\\'+file)
        print(True, datfilename)
        # testsolution = ediudf.makeudf(filename)
    else:
        print(False)
        continue


# udf_string = ediudf.makeudf('sample1.edi')

# text_file = open("C:\Transfer\output.udf", "w")
# text_file.write(udf_string)
# text_file.close()