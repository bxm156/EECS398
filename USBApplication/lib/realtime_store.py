import Queue
import datetime

class RealTimeStore(object):

    voltage_queue = Queue.Queue()
    current_queue = Queue.Queue()

    def put(self, sql_rows):
        if not sql_rows:
            return
        zipped = zip(*sql_rows)
        epochs = zipped[0]
        epochs = map(lambda x: datetime.datetime.fromtimestamp(x), epochs)
        voltages = zipped[1]
        currents = zipped[2]
        for i in xrange(len(epochs)):
            self.voltage_queue.put((epochs[i], voltages[i],))
            self.current_queue.put((epochs[i], currents[i],))
        
    def next_voltage(self):
        try:
            return self.voltage_queue.get_nowait()
        except Queue.Empty:
            return False

    def next_current(self):
        try:
            return self.current_queue.get_nowait()
        except Queue.Empty:
            return False

    def clear(self):
        pass 
