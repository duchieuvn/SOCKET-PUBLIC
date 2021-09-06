import pyodbc

SERVER = 'MON-PC\SQLEXPRESS'
DATABASE = 'Socket_Account'

#print(pyodbc.drivers())

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                        SERVER=' + SERVER + ';DATABASE= ' + DATABASE +'; \
                        UID=dh; PWD=123456;')

#DRIVER={SQL Server}; SERVER=TestServer; Database=TestDatabase; UID=UserID; PWD=Password;')


#ODBC Driver 17 for SQL Server