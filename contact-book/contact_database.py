import logging as log
import sqlite3 as sqlite
from sqlite3 import Error

class ContactDatabase:
    def __init__(self):
        self.conn = None

    def create_connection(self, db_file):
        try:
            self.conn = sqlite.connect(db_file)
            log.info('Connection established')
            self.cursor = self.conn.cursor()
            return self.conn
        except Error as e:
            log.error(e)

    def create_contacts_table(self):
        sql_create_contacts_table = """ CREATE TABLE IF NOT EXISTS contacts (
                                        id integer PRIMARY KEY,
                                        first_name text NOT NULL,
                                        last_name text
                                    ); """
        try:
            self.cursor.execute(sql_create_contacts_table)
        except Error as e:
            log.error(e)

    def create_contact(self, contact):
        sql = ''' INSERT INTO contacts(first_name,last_name)
                  VALUES(?,?) '''
        try:
            self.cursor.execute(sql, contact)
            return self.cursor.lastrowid
        except Error as e:
            log.error(e)

    def print_contacts(self, contacts):
        data = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'c']]

        col_width = max(len(word) for row in data for word in row) + 2  # padding
        for row in data:
            print("".join(word.ljust(col_width) for word in row))

    def close_connection(self):
        self.conn.close()

    def __del__(self):
        if self.conn:
            log.info('Closing connection')
            self.conn.close()


def test():
    log.basicConfig(level=log.INFO)
    db = ContactDatabase()
    db.create_connection(':memory:')
    db.create_contacts_table()
    db.create_contact(('John', 'Doe'))
    db.print_contacts(None)

if __name__ == "__main__":
    test()

