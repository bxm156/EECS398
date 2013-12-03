from threads.task_thread import  TaskThread
from lib.packet_decoder import PacketDecoder
from lib.lib import Packet
from bitstring import Bits
import serial
import numpy
import cStringIO
import datetime
import sys

class SerialThread(TaskThread):

    def __init__(self, serial_path, work_queue, wattrlib):
        super(SerialThread, self).__init__(work_queue)
        self.serial_path = serial_path
        assert self.serial_path
        self.serial_connection = None
        self.wattrlib = wattrlib
        self.packet_decoder = PacketDecoder(lambda x: wattrlib.insert_data(x))

    def setup(self):
        self.connect()

    def connect(self):
        self.serial_connection = serial.Serial(self.serial_path, timeout=1, baudrate=115200)

    def cleanup(self):
        self.disconnect()

    def disconnect(self):
        self.serial_connection.close()

    def handle_task(self, task):
        task.run(self.serial_connection)

    def idle(self):
        #Read data when we have no user requested tasks
        #input_bytes = self.serial_connection.read(560)
        #self.packet_decoder.push(Bits(bytes=input_bytes))
        #self.packet_decoder.handle()
        line = self.serial_connection.readline()
        try:
            data = numpy.genfromtxt(cStringIO.StringIO(line), dtype=(int,int,int,float,float,float,float,float,float,float,float), delimiter=",")
            datetime.datetime.fromtimestamp(int(data['f0']))
            p = Packet(
                flags=int(data['f2']),
                epoch=int(data['f0']),
                voltage=float(data['f3']),
                current=float(data['f4']),
                period=float(data['f5']),
                active_power=float(data['f6']),
                reactive_power=float(data['f8']),
                apparent_power=float(data['f7']),
                phase_angle=float(data['f10']),
                power_factor=float(data['f9']),
            )
            self.wattrlib.insert_data([p])
        except:
            pass
