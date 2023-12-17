#!/usr/bin/python3
"""lists all cities of that state, using the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cursor.fetchall()
    tm = list(row[0] for row in rows)
    print(*tm, sep=", ")
    cursor.close()
    db.close()
