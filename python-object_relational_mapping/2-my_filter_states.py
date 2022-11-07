#!/usr/bin/python3
''''
Select all lists from the database hbtn_0e_0usa
'''
import MySQLdb
import sys


class DataBase:
    '''
    Class representing connection to MySQL database
    '''
    def __init__(self, arg_user, arg_password, arg_database, arg_name_searched):
        self.user = arg_user
        self.password = arg_password
        self.database = arg_database
        self.name_searched = arg_name_searched
        db = MySQLdb.Connect(
                            host='localhost',
                            port=3306,
                            user=self.user,
                            password=self.password,
                            db=self.database
                            )
        self.cur = db.cursor()

    def print_all_states(self):
        self.cur.execute("SELECT * FROM states")
        all_states = self.cur.fetchall()
        for states in all_states:
            if states[1][0] == "N":
                print(f"({states[0]}, '{states[1]}')")

    def name_to_search(self, name_searched):
        search_consult = "SELECT * FROM states WHERE name='{}'".format(name_searched)
        self.cur.execute(search_consult)
        all_name_searched = self.cur.fetchall()
        for name_db in all_name_searched:
                print("{}".format(name_db))


if __name__ == "__main__":
    args = sys.argv
    arg_user = args[1]
    arg_password = args[2]
    arg_database = args[3]
    arg_name_searched = args[4]
    all_states = DataBase(arg_user, arg_password, arg_database, arg_name_searched)
    all_states.name_to_search(arg_name_searched)
