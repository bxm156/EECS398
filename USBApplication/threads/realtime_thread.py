from threads.base_thread import BaseThread
import time


class RealTimeThread(BaseThread):

    def __init__(self, wattrlib):
        super(RealTimeThread, self).__init__()
        self.wattrlib = wattrlib
        self.last_date = 0#int(time.time())

    def loop(self):
        self.wattrlib.get_realtime_data(self.last_date, self.update_store)  
        time.sleep(0.05)

    def update_store(self, task):
        results = task.get_result()
        if results:
            self.wattrlib.get_realtime_store().put(results)
            last_row = results[-1]
            self.last_date = int(last_row[0])

