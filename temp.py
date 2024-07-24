# importing module
import oracledb
# Inserting a record into a table in Oracle database
try:
    con = oracledb.connect(user = 'system', password = 'jvdpLNS23510', host = 'localhost')
    cursor = con.cursor()

    # con.autocommit = True
    # Inserting a record into table employee

    # cursor.execute('insert into employee values(10001,\'Rahul\',50000.50)')

    # commit() to make changes reflect in the database

    # con.commit()
    # print('Record inserted successfully')
    while True:
        operation : str
        operation = input("Register / Login")
        if(operation == 'Register'):
            cursor.execute()

except oracledb.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation