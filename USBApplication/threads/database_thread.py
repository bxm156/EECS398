import sqlite3
from threads.task_thread import TaskThread
from tasks.sqlite.create_task import SQLiteCreateTask


class DatabaseThread(TaskThread):

    def __init__(self, connection_string, work_queue, idle_task=None):
        super(DatabaseThread, self).__init__(work_queue=work_queue)
        self.connection_string = connection_string
        assert self.connection_string
        self.idle_task = idle_task

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

    def idle(self):
        if self.idle_task:
            self.idle_task.run(self.connection)
            if self.idle_task.listener:
                self.idle_task.listener(self.idle_task)
