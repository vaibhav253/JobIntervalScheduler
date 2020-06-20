import MySQLdb
#connection to mySQL server
class connection():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="jobs")

    #db.close()
#connection()