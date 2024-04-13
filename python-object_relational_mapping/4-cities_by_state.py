#!/usr/bin/python3
"""
    Connects to a MySQL server and retrieves a list of cities from specified database.
    
    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database containing the cities table.
    
    Returns:
        None
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
