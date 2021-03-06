from datetime import datetime

from tasks.sqlite_task import SQLiteTask


class SQLiteSelectTask(SQLiteTask):

    query = "SELECT * FROM data WHERE epoch >= :start_time AND epoch <= :end_time"

    def run(self, connection):
        super(SQLiteSelectTask, self).run(connection)
        cur = connection.cursor()
        cur.execute(self.query, self.parameters)
        self.result = cur.fetchall()
