#!/usr/bin/python3
''''
Select all lists from the database hbtn_0e_0usa
'''
import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.Connect(
                    host='localhost',
                    port=3306,
                    user=argv[1],
                    password=argv[2],
                    db=argv[3]
                    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name='{:s}'ORDER BY id ASC"
        .format(argv[4])
        )
    for row in cursor.fetchall():
            print("{}".format(row))