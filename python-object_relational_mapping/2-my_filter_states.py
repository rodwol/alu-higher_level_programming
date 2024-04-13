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


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         username=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)

    cursor = db.cursor()
    states_name=sys.argv[4]
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql_query, (state_name,))

    states = cursor.fetchall()
    for i in states:
        print(i)

    cursor.close()
    db.close()
