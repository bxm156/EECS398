import sqlite3
import base_thread

from tasks.sqlite.create_task import SQLiteCreateTask


class DatabaseThread(base_thread.BaseThread):

    def __init__(self, connection_string, work_queue):
        super(DatabaseThread, self).__init__(work_queue=work_queue)
        self.connection_string = connection_string
        assert self.connection_string

    def setup(self):
        self.connect()
        self.work_queue.put(SQLiteCreateTask())

    def connect(self):
        self.connection = sqlite3.connect(self.connection_string)
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.connection.execute("PRAGMA synchronous = OFF")
        self.connection.execute("PRAGMA journal_mode = MEMORY;")

    def cleanup(self):
        self.disconnect()

    def disconnect(self):
        self.connection.close()

    def handle_task(self, task):
        task.run(self.connection)
