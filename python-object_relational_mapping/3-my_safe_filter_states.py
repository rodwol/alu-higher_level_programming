#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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
