import random

class Contact:
    def __init__(self, first_name, last_name=None):
        """
        https://stackoverflow.com/a/4843178/1061279
        """
        if not isinstance(first_name, str): raise TypeError(first_name)
        self.first_name = first_name
        self.last_name = last_name
        self.id = random.randrange(10)

def main():
    """"""
    c = Contact(last_name="Doe", first_name="John")
    print(c.first_name)
    print(c.last_name)
    print(c.id)


if __name__ == "__main__":
    main()
