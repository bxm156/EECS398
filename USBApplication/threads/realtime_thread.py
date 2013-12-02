from threads.base_thread import BaseThread
import time
import threading

class RealTimeThread(BaseThread):

    lock = threading.Lock()

    def __init__(self, wattrlib):
        super(RealTimeThread, self).__init__()
        self.wattrlib = wattrlib
        self.since_date = 0 #int(time.time()) - 12*60*60

    def loop(self):
        self.lock.acquire()
        def update_store(task):
            results = task.get_result()
            if results:
                self.wattrlib.get_realtime_store().put(results)
                last_row = results[-1]
                self.since_date = int(last_row[0])
            self.lock.release()
        self.wattrlib.get_realtime_data(self.since_date, update_store)


