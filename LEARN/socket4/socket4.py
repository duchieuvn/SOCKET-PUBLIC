import pyodbc


#print(pyodbc.drivers())

conx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=MON-ASUS\SQLEXPRESS; Database=Socket_Account; UID=dh; PWD=123456;')



# cursor = conx.cursor()
# for row in cursor.execute("select username from Account"):
#     print(row)

# cursor.execute("insert Account values ('dh', '123')")
# conx.commit()

# conx.close()

