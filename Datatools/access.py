# import pyodbc

# db_path = "C:\\Users\\apiispanen\\Documents\\OA Project\\AGT\\AGT.accdb"
# connect_str = 'DRIVER=(Microsoft Access Driver (*.mdb));DBQ=%s' %(db_path)
# # print(connect_str)
# # connection = pyodbc.connect(connect_str)

# conn = pyodbc.connect(('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\apiispanen\\Documents\\OA_Project\\TGP\\DB4_TGP.accdb;')
# cursor = conn.cursor()
# cursor.execute('select * from tracking_sales')
   
# for row in cursor.fetchall():
#     print (row)



import pyodbc
print(pyodbc.drivers())

# blah = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]
# print(blah)