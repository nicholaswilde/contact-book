import sqlite3 as sqlite


class ContactDatabase:
    def __init__(self):
        self.conn = None

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        try:
            self.conn = sqlite.connect(db_file)
            print(sqlite.version)
        except Error as e:
            print(e)
        return self.conn

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def close_connection(self):
        self.conn.close()


    def __del__(self):
        if self.conn != None:
            print(f'Closing connection')
            self.conn.close()


def test():
    contacts_table = "contacts"
    db = ContactDatabase()
    db.create_connection(':memory:')
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    db.create_table(sql_create_projects_table)


if __name__ == "__main__":
    test()

