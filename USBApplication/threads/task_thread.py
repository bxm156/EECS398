import sqlite3
import threading
import time
import Queue

from threads.base_thread import BaseThread

class TaskThread(BaseThread):

    def __init__(self, work_queue):
        super(BaseThread, self).__init__()
        self.work_queue = work_queue
        self.should_terminate = threading.Event()
 
    def setup(self):
        pass

    def join(self, timeout=None):
        self.should_terminate.set()
        super(BaseThread, self).join(timeout)

    def handle_task(task):
        raise NotImplementedError

    def cleanup(self):
        pass

    def idle(self):
        pass

    def loop(self):
        try:
            task = self.work_queue.get(True, 0.0001)
            self.handle_task(task)
            if task.listener:
                task.listener(task)
        except Queue.Empty:
            self.idle()

