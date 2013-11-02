import base_thread


class SerialThread(base_thread.BaseThread):

    def __init__(self, serial_path, work_queue):
        super(SerialThread, self).__init__(work_queue=work_queue)
        self.serial_path = serial_path
        self.serial_connection = None
        assert self.serial_path

    def setup(self):
        self.connect()

    def connect(self):
        pass

    def cleanup(self):
        pass

    def disconnect(self):
        pass

    def handle_task(task):
        pass
