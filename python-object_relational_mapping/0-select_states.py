#!/usr/bin/python3
"""
Module: lists all states from the database hbtn_0e_0_usa

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


