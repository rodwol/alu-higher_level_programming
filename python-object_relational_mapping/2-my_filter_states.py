#!/usr/bin/python3
"""
Module: Script to search for states in a MySQL database table.

Usage:
    ./search_states.py [mysql_username] [mysql_password]
     [database_name] [state_name]

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
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    cursor = db.cursor()
    sql_query = "SELECT * FROM states WHERE name = '{}'\
ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(sql_query)

    states = cursor.fetchall()
    for i in states:
        print(i)

    cursor.close()
    db.close()
