#!/usr/bin/python3
import MySQLdb
import sys
"""lists all states from the database hbtn_0e_0_usa:"""


if __name__ == "__main__":
    user, passw, database = sys.argv[1], sys.argv[2], sys.argv[3]
    query = """SELECT * FROM states ORDER BY id ASC;"""
    dbase = MySQLdb.connect(
        host="localhost",
        port=3306, user=user, passwd=passw,
        db=database, charset="utf8"
    )
    mouse = dbase.cursor()
    mouse.execute(query)
    rows = mouse.fetchall()
    for row in rows:
        print(row)

    mouse.close()
    dbase.close()

    # print(f"User: {user}, Password: {passw}, Database: {database}")
