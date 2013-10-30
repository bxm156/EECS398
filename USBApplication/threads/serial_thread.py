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
        self.connection = sqlite3.connect(self.connection_string)
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.connection.execute("PRAGMA synchronous = OFF")
        self.connection.execute("PRAGMA journal_mode = MEMORY;")

    def cleanup(self):
        self.disconnect()

    def disconnect(self):
        self.connection.close()

    def handle_task(task):
        task.run(self.connection)
