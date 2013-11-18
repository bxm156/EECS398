import time

from tasks.serial_task import SerialTask


class ReadTask(SerialTask):

    def run(self, serial_connection):
        self.result = []
        serial_connection.write("get_stats,%f" % (time.mktime(self.parameters['datetime']),))
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
        self.result.append(tuple(line.split(',')))
