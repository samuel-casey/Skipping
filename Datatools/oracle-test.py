import cx_Oracle

connection = cx_Oracle.connect('cci/WElcome#_321@129.213.41.220:1521/ccipdb.sub02151456220.ccipaasvcn.oraclevcn.com')
cur = connection.cursor()
cur.execute('my query')
for result in cur:
    print(result)
cur.close()
connection.close()