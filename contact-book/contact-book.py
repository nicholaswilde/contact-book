import sys
from contact_database import ContactDatabase

MIN_PYTHON = (3,6)
if sys.version_info<MIN_PYTHON:
    sys.exit('Python %s.%s or later is required.\n' % MIN_PYTHON)

from cmd import Cmd
import os

class ContactBookPrompt(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = 'cb> '
        self.intro  = 'Welcome to contact-book! Type ? to list commands'
        self.do_EOF = self.do_exit
        self.help_EOF = self.help_exit
        self.db = ContactDatabase()
        self.file = None

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_add(self, inp):
        print("adding '{}'".format(inp))

    def help_add(self):
        print("Add a new entry to the system.")

    def do_list(self, ignore):
        contacts = self.db.get_all_contacts()
        self.db.print_contacts(contacts)

    def do_create(self, inp):
        print(inp)
        t = tuple(filter(None, inp.split(' ')))
        self.db.create_contact(t)

    def help_list(self):
        print("List all contacts")

    def do_open(self, inp):
        self.file = inp
        self.db.create_connection(inp)
        #self.db.create_contacts_table()

    def help_open(self):
        print("Open a database file")

    '''def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))
    '''

def main():
    db = ContactDatabase()
    db.create_connection(':memory:')
    db.create_contacts_table()
    db.create_contact(('John', 'Doe'))
    ContactBookPrompt().cmdloop()

if __name__ == "__main__":
    main()
