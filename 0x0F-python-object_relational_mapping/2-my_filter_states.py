#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def lister(user, passw, database, argumnt):
    """the function to connect to and list the database"""
    query = """
    SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC
    """.format(argumnt)
    db = MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=passw, db=database)
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    user, passw = sys.argv[1], sys.argv[2]
    database, argumnt = sys.argv[3], sys.argv[4]
    lister(user, passw, database, argumnt)
