import os
import pandas as pd
year = 2018
directory = 'V:\\Op_Avail\\TGP\\2017\\EBB2'
os.chdir(directory)
# print(os.listdir())
# for file in os.listdir():
#     with open(file, 'r')



read = pd.read_excel("DEL_ID3_0206174421.xls", sheet_name='WorkSheet1', index_col = 3)
print('1/28/2018' in read, type(read))

# xls = pd.ExcelFile("DEL_ID3_0206174421.xls")

# sheetX = xls.parse(0) #2 is the sheet number

# var1 = sheetX['WorkSheet1']
# print(var1[1]) 