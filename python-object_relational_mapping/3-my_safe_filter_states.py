#!/usr/bin/python3
"""
Once again, write a script that takes in arguments
and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that
is safe from MySQL injections!
"""
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    row = cur.fetchall()
    for r in row:
        print(r)
