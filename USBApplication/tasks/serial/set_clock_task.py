import time

from tasks.serial_task import SerialTask

class SetClockTask(SerialTask):


    def run(self, serial_connection):
        serial_connection.write("set_clock,%f" % (time.mktime(self.parameters['datetime']),))
        self.result = serial_connection.readline()

