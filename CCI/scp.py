import pyodbc
# print(pyodbc.drivers())
# conn = pyodbc.connect('Driver = {SQL Server};'
#                     'Server=129.213.41.220;'
#                     'Database=ccipdb.sub02151456220.ccipaasvcn.oraclevcn.com') 

# Server = '129.213.41.220'
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\apiispanen\\Documents\\OA_Project\\TGP\\TGP_DB.accdb;")
cursor = conn.cursor()
cursor.execute('select * FROM MPF1;')
for row in cursor:
    print(row)
   
# for row in cursor.fetchall():
#     print (row)
