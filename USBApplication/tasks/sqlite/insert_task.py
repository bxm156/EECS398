from tasks.sqlite_task import SQLiteTask


class SQLiteInsertTask(SQLiteTask):
    """Accepts list of tuples as the parameters"""


    query = "INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?,?)"

    def set_values(self, tuple_list):
        self.tuple_list = tuple_list

    def run(self, connection):
        assert self.tuple_list
        cur = connection.cursor()
        print self.tuple_list
        cur.executemany(self.query, self.tuple_list)
        connection.commit()

