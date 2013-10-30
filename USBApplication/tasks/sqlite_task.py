import sqlite3

from base_task import BaseTask


class SQLiteTask(BaseTask):


    def run(self, connection):
        raise NotImplementedError

    def cleanup(self):
        pass
