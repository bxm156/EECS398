import base_thread
import serial

class SerialThread(base_thread.BaseThread):

    def __init__(self, serial_path, work_queue):
        super(SerialThread, self).__init__(work_queue=work_queue)
        self.serial_path = serial_path
        self.serial_connection = None
        assert self.serial_path

    def setup(self):
        self.connect()

    def connect(self):
        self.serial_connection = serial.Serial(self.serial_path, timeout=1)

    def cleanup(self):
        self.disconnect()

    def disconnect(self):
        self.serial_connection.close()

    def handle_task(self, task):
        task.run(self.serial_connection)
