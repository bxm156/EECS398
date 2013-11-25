from threads.task_thread import  TaskThread
from lib.packet_decoder import PacketDecoder
from bitstring import Bits
import serial

class SerialThread(TaskThread):

    def __init__(self, serial_path, work_queue, wattrlib):
        super(SerialThread, self).__init__(work_queue)
        self.serial_path = serial_path
        assert self.serial_path
        self.serial_connection = None
        self.packet_decoder = PacketDecoder(lambda x: wattrlib.insert_data(x))

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

    def idle(self):
        #Read data when we have no user requested tasks
        input_bytes = self.serial_connection.read(560)
        self.packet_decoder.push(Bits(bytes=input_bytes))
        self.packet_decoder.handle()
