from datetime import datetime

from tasks.sqlite_task import SQLiteTask


class SQLiteSelectTask(SQLiteTask):

    query = "SELECT * FROM data WHERE timestamp >= :start_time AND timestamp <= :end_time"
    parameters = None

    def run(self, connection):
        assert self.parameters
        cur = connection.cursor()
        cur.execute(self.query, self.parameters)
        self.results = cur.fetchall()
