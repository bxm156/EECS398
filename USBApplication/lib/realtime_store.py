import Queue
import datetime

class RealTimeStore(object):

    voltage_queue = Queue.Queue()
    current_queue = Queue.Queue()
    period_queue = Queue.Queue()
    active_power_queue = Queue.Queue()
    reactive_power_queue = Queue.Queue()
    apparent_power_queue = Queue.Queue()
    phase_angle_queue = Queue.Queue()
    power_factor_queue = Queue.Queue()

    def put(self, sql_rows):
        if not sql_rows:
            return
        zipped = zip(*sql_rows)
        epochs = zipped[0]
        epochs = map(lambda x: datetime.datetime.fromtimestamp(x), epochs)
        voltages = zipped[1]
        currents = zipped[2]
        periods = zipped[2]
        active_powers = zipped[2]
        reactive_powers= zipped[2]
        apparent_powers = zipped[2]
        phase_angles = zipped[2]
        power_factors = zipped[2]
        for i in xrange(len(epochs)):
            self.voltage_queue.put((epochs[i], voltages[i],))
            self.current_queue.put((epochs[i], currents[i],))
            self.period_queue.put((epochs[i], periods[i],))
            self.active_power_queue.put((epochs[i], active_powers[i],))
            self.reactive_power_queue.put((epochs[i], reactive_powers[i],))
            self.apparent_power_queue.put((epochs[i], apparent_powers[i],))
            self.phase_angle_queue.put((epochs[i], phase_angles[i],))
            self.power_factor_queue.put((epochs[i], power_factors[i],))
        
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
