import logging as log

class Contact:
    def __init__(self, contact):
        if not isinstance(contact, tuple): raise TypeError(contact)
        self.id = contact[0]
        self.first_name = contact[1]
        self.last_name = contact[2]

    def to_tuple(self):
        l = [value for value in vars(self).values()]
        t = tuple(l)
        return t


def main():
    log.basicConfig(level=log.INFO)
    c = Contact((1, "Doe", "John"))
    log.info(c.first_name)
    log.info(c.last_name)
    log.info(c.id)
    log.info(c.to_tuple())


if __name__ == "__main__":
    main()
