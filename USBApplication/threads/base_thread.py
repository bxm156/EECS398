import sqlite3
import threading
import time
import Queue


class BaseThread(threading.Thread):

    def __init__(self, work_queue, default_sleep=1):
        super(BaseThread, self).__init__()
        self.work_queue = work_queue
        self.should_terminate = threading.Event()
        self.default_sleep = default_sleep

    def join(self, timeout=None):
        self.should_terminate.set()
        super(BaseThread, self).join(timeout)

    def handle_task(task):
        raise NotImplementedError

    def cleanup(self):
        pass

    def run(self):
        while not self.should_terminate.is_set():
            try:
                task = self.work_queue.get(True, 0.05)
                self.handle_task(task)
            except Queue.Empty:
                continue
        # Cleanup
        self.cleanup()
