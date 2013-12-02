import Queue
import datetime
from types import READING

class RealTimeStore(object):

    voltage_queue = Queue.Queue()
    current_queue = Queue.Queue()
    period_queue = Queue.Queue()
    active_power_queue = Queue.Queue()
    reactive_power_queue = Queue.Queue()
    apparent_power_queue = Queue.Queue()
    phase_angle_queue = Queue.Queue()
    power_factor_queue = Queue.Queue()


    def __init__(self):
        self.queue_map = {
            READING.VOLTAGE: self.voltage_queue,
            READING.CURRENT: self.current_queue,
            READING.PERIOD: self.period_queue,
            READING.ACTIVE_POWER: self.active_power_queue,
            READING.APPARENT_POWER: self.apparent_power_queue,
            READING.PHASE_ANGLE: self.phase_angle_queue,
            READING.POWER_FACTOR: self.power_factor_queue,
       }


    def put(self, sql_rows):
        if not sql_rows:
            print "Put no rows"
            return
        zipped = zip(*sql_rows)
        epochs = zipped[0]
        epochs = map(lambda x: datetime.datetime.fromtimestamp(x), epochs)
        voltages = zipped[1]
        currents = zipped[2]
        periods = zipped[3]
        active_powers = zipped[4]
        reactive_powers= zipped[5]
        apparent_powers = zipped[6]
        phase_angles = zipped[7]
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

    def next_reading(self, rtype):
        try:
            return self.queue_map[rtype].get_nowait()
        except Queue.Empty:
            return False

    def clear(self):
        pass 
