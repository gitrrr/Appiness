import MySQLdb

def databaseConnection():
    connection = MySQLdb.connect(host="localhost",
                                 user="root",
                                 passwd="password",
                                 db="Appiness")
    return connection
