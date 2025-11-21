import mysql.connector
print("db file priniting statement")
def db_connection_func():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    database="d5_pdbc",
    password ="Vamsi@1231310"
)