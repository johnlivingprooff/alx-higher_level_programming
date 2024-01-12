#!/usr/bin/python3
import MySQLdb
import sys
"""lists all states from the database hbtn_0e_0_usa:"""


def lister(user_n, passw, database):
    """this function does all the querying"""

    query = "SELECT * FROM states ORDER BY id ASC;"
    dbase = MySQLdb.connect(
        host="localhost", port=3306, user=user_n, passwd=passw, db=database
    )
    mouse = dbase.cursor()
    mouse.execute(query)
    rows = mouse.fetchall()

    for row in rows:
        print(row)

    mouse.close()
    dbase.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    user_n = sys.argv[1]
    passw = sys.argv[2]
    database = sys.argv[3]

    lister(user_n, passw, database)
