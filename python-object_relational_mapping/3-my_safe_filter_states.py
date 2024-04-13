#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

This script connects to a MySQL database and retrieves data from the 'states' table
based on a provided argument. It takes four command-line arguments:
1. MySQL username
2. MySQL password
3. MySQL database name
4. Name to search for in the 'name' column of the 'states' table

Usage: ./script_name.py <username> <password> <database_name> <name_to_search>
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    cursor = db.cursor()
    sql_query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]
    cursor.execute(sql_query)
    states = cursor.fetchall()
    for i in states:
        print(i)

    cursor.close()
    db.close()
