#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def lister(user, passw, database):
    """core function"""
    query = """
        SELECT cities.id, cities.name AS city_name, states.name AS state_name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
        """
    dbase_conn = MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=passw, db=database)
    mouse = dbase_conn.cursor()
    mouse.execute(query)

    rows = mouse.fetchall()
    for row in rows:
        print(row)

    mouse.close()
    dbase_conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        lister(sys.argv[1], sys.argv[2], sys.argv[3])
