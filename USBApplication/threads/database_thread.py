import sqlite3
import base_thread


class DatabaseThread(base_thread.BaseThread):

    def __init__(self, db_path, work_queue):
        super(DatabaseThread, self).__init__(work_queue=work_queue)
        self.db_path = db_path
        assert self.db_path
        self.db_connection = None

    def connect(self):
        self.db_connection = sqlite3.connect(self.db_path)

    def disconnect(self):
        pass

    def handle_task(task):
        pass
