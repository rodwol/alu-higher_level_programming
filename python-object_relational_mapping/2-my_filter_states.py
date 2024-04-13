#!/usr/bin/python3
"""
Module: Script to search for states in a MySQL database table.

Usage:
    ./search_states.py [mysql_username] [mysql_password] [database_name] [state_name]

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Name of the database
    state_name: Name of the state to search for

Example:
    ./search_states.py root password hbtn_0e_0_usa California
"""
import sys
import MySQLdb


def search_states(username, password, database, state_name):
    db = MySQLdb.connect(host='localhost',
                         username=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)

    cursor = db.cursor()
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql_query, (state_name,))

    states = cursor.fetchall()
    for i in states:
        print(i)

    cursor.close()
    db.close()

if __name__ == "__main__":
    state_name = sys.argv[4]
    search_states(username, password, database, state_name)
