from task.sqlite_task import SQLiteTask


class SQLiteInsertTask(SQliteTask):
    """Accepts list of tuples as the parameters"""


    query = "INSERT INTO data VALUES(?,?,?,?,?,?,?,?)"

    def run(self, connection):
        assert self.parameters
        cur = connection.cursor()
        cur.executemany(self.query, self.parameters)

