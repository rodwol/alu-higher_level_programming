#!/usr/bin/python3
"""
Module: lists all states with a name
Starting with N (upper N) from the database hbtn_0e_0_usa
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
