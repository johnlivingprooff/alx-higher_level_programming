#!/usr/bin/python3
import MySQLdb
import sys
"""lists all states from the database hbtn_0e_0_usa:"""


def lister(user, passw, database):
    """the function to connect to and list the database"""
    db = MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=passw, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    user, passw, database = sys.argv[1], sys.argv[2], sys.argv[3]
    print(f"User: {user}, Password: {passw}, Database: {database}")
    lister(user, passw, database)
