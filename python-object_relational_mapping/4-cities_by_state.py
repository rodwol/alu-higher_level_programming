#!/usr/bin/python3
"""
Module Name: DatabaseCityState.py

Description:
This module connects to a MySQL database and retrieves information about cities

Dependencies:
- MySQLdb: A library that provides an interface for connecting to MySQ

Usage:
This module can be executed from the command line with three arguments:
1. MySQL username
2. MySQL password
3. MySQL database name

Example Command:
python DatabaseCityState.py <username> <password> <database_name>
"""
import sys
import MySQLdb


if __name__ == '__main__':
    connect = MySQLdb.connect(host='localhost',
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              port=3306)

    cursor = connect.cursor()
    sql_query = "SELECT  cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id=states.id"
    cursor.execute(sql_query)
    cities = cursor.fetchall()
    for i in cities:
        print(i)

    cursor.close()
    connect.close()
