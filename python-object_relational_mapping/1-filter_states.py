#!/usr/bin/python3
"""
Module: lists all states with a name
Starting with N (upper N) from the database hbtn_0e_0_usa

This script connects to the MySQL server running on localhost using
the provided username, password, and database name. It then executes
a query to retrieve all states whose names start with 'N' and
displays the results sorted by the state id.
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE Binary\
name LIKE 'N%' ORDER BY id ASC")
    states_data = cursor.fetchall()
    for i in states_data:
        print(i)

    cursor.close()
    db.close()
