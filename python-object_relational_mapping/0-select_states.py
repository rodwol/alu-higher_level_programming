#!/usr/bin/python3
"""
Module: This script lists all states from the database hbtn_0e_0_usa.

This script connects to a MySQL database and retrieves the list of states from the 'states' table.
It then prints out the retrieved data.

Usage:
    python3 script_name.py <username> <password> <database_name>
"""
import sys
import MySQLdb


def list_states(username, password, database):
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT *FROM states ORDER BY id ASC")
    states_data = cursor.fetchall()
    for i in states_data:
        print(i)

    db.close()

if __name__ == "__main__":
    list_states(username, password, database)
