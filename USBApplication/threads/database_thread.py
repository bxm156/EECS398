import sqlite3
import threading
import time
import Queue

class DatabaseThread(threading.Thread):

    def __init__(self, db_path, work_queue):
        super(DatabaseThread, self).__init__()
        self.db_path = db_path
        assert self.db_path
        self.db_connection = None
        self.work_queue = work_queue
        self.should_terminate = threading.Event()

    def connect(self):
        self.db_connection = sqlite3.connect(self.db_path)

    def disconnect(self):
        pass

    def join(self, timeout=None):
        self.should_terminate.set()
        super(DatabaseThread, self).join(timeout)

    def run(self):
        while not self.should_terminate.is_set():
            try:
                work = self.work_queue.get()
            except Queue.Empty:
                continue
            time.sleep(1)
        # Cleanup
