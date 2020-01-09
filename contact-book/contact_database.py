from log import log
import sqlite3 as sqlite
from sqlite3 import Error


def _get_col_width(data):
    return max(len(str(word)) for row in data for word in row) + 2 # Padding


def _format_header(value):
    value = value.replace('_',' ')
    value = value.title()
    return value


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
            self.conn.commit()
            return self.cursor.lastrowid
        except Error as e:
            log.error(e)

    def get_header(self, format_header=True):
        self.get_all_contacts()
        header_list = []
        if self.cursor.description:
            header_list = [value[0] for value in self.cursor.description]
            if format_header:
                header_list = map(_format_header, header_list)
        t = tuple(header_list)
        return t

    def _add_header(self, contacts):
        header_list = self.get_header(True)
        contacts.insert(0, header_list)
        separator_list = ["".ljust(len(str(word)), '-') for word in header_list]
        contacts.insert(1, separator_list)
        return contacts

    def print_contacts(self, contacts, include_header=True):
        if include_header:
            contacts = self._add_header(contacts)
        col_width = _get_col_width(contacts)
        for row in contacts:
            print("".join(str(word).ljust(col_width) for word in row))

    def get_all_contacts(self):
        try:
            self.cursor.execute("SELECT * FROM contacts")
            return self.cursor.fetchall()
        except Error as e:
            log.error(e)

    def close_connection(self):
        self.conn.close()

    def __del__(self):
        if self.conn:
            log.info('Closing connection')
            self.conn.close()


def test():
    db = ContactDatabase()
    db.create_connection(':memory:')
    db.create_contacts_table()
    db.create_contact(('John', 'Doe'))
    contacts = db.get_all_contacts()
    print(db.print_contacts(contacts))

if __name__ == "__main__":
    test()

