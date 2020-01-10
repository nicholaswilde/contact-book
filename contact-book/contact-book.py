import sys

MIN_PYTHON = (3,6)
if sys.version_info<MIN_PYTHON:
    sys.exit('Python %s.%s or later is required.\n' % MIN_PYTHON)

import os
from cmd import Cmd
from builtins import any as b_any
from log import log
from contact_database import ContactDatabase

dirname = os.path.dirname(__file__)

DEFAULT_DB = os.path.join(dirname, '../data/contact-book.db')

class ContactBookPrompt(Cmd):
    def __init__(self, input_file):
        Cmd.__init__(self)
        self.prompt = 'cb> '
        self.intro  = 'Welcome to contact-book! Type ? to list commands'
        self.do_EOF = self.do_exit
        self.help_EOF = self.help_exit
        self.db = ContactDatabase()
        self.do_open(input_file)

    def do_add(self, inp):
        d = _parse_input(inp)

    def help_add(self):
        print("Add a new entry to the system.")

    def do_create(self, inp):
        print(inp)
        t = tuple(filter(None, inp.split(' ')))
        self.db.create_contact(t)

    def help_create(self):
        print("create FIRST_NAME [LAST_NAME]\tCreate a new contact")

    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print("Exit the application. Shorthand: x q Ctrl-D.")

    def do_file(self, ignore):
        print(self.file)

    def help_file(self):
        print('List the database file')

    def do_list(self, ignore):
        contacts = self.db.get_all_contacts()
        self.db.print_contacts(contacts)

    def help_list(self):
        print("List all contacts")

    def do_open(self, inp):
        if inp:
            self.file = inp
            self.db.create_connection(inp)
            self.db.create_contacts_table()
        else:
            print("Please add an argument")

    def help_open(self):
        print('open FILE\tOpen a database file')

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

def _parse_input(inp):
    l = list(filter(None, inp.split(' ')))

    if b_any("=" in x for x in l):
        character = "="
        l = [m.split(character, 1) for m in l]
    elif b_any(":" in x for x in l):
        character = ":"
        l = [m.split(character, 1) for m in l]

    d = {}
    if l:
        d = dict(l)
    return d

def main():
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    elif len(sys.argv) == 1:
        input_file = DEFAULT_DB
    else:
        log.error('Too many arguments were given')
        sys.exit()
    cbp = ContactBookPrompt(input_file)
    cbp.cmdloop()

if __name__ == "__main__":
    main()
