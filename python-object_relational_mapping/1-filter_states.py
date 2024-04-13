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


def states_starting_with_n(username, password, database):
    db = MySQLdb.connect(host="localhost",
                         username=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states_data = cursor.fetchall()
    for i in states_data:
        print(i)

    cursor.close()
    db.close()

if __name__ == "__main__":
