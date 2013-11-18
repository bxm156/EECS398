import time

from tasks.serial_task import SerialTask


class TestTask(SerialTask):

    def run(self, serial_connection):
        self.x = 1
        while True:
            serial_connection.write('TEST\n')
            recieved_data = False
            while True:
                line = serial_connection.readline()
                line = line.rstrip()
                if line == "END":
                    break
                elif line == "":
                    continue
                else:
                    self.handle_line(line)

    def handle_line(self, line):
        print self.x
        self.x += 1
        
