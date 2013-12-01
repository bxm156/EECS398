from bitstring import BitStream
import struct

from lib import Packet

class PacketDecoder(object):

    HEADER = '0x59'
    FOOTER = '0x5254464d'
    LENGTH = 56*8
    PATTERN = "2BH9I8B2I"

    packet_store = []

    def __init__(self, listener_func):
        self.listener_func = listener_func
        self.stream = BitStream()

    def push(self, byte_array):
        self.stream.append(byte_array) 

    def handle(self):
        while True:
            if len(self.stream) < self.LENGTH:
                break

            #Look for a header
            header_pos = self.stream.find(self.HEADER)
            if header_pos:
                header_pos = header_pos[0]
            else:
                self.stream.clear()
                break

            end_pos = header_pos + self.LENGTH
            if len(self.stream) < end_pos:
                # Not Enough Data
                break

            # Extract potential packet
            potential_packet = self.stream[header_pos:end_pos].bytes
            valid_packet = self.analyze_packet(potential_packet)
            if valid_packet:
                self.stream = self.stream[end_pos:]
            else:
                self.stream = self.stream[header_pos+1:]
        self.save_packets()
        self.packet_store = []

    def analyze_packet(self, byte_string):
        if len(byte_string) != 56:
            return
        data =  struct.unpack(self.PATTERN, byte_string)
        header = data[0]
        footer = data[21]
        if hex(header) == self.HEADER and hex(footer) == self.FOOTER:
            if self.validate_checksums(data):
                packet = self.create_packet(data)
                self.packet_store.append(packet)
                return True
        return False

    def validate_checksums(self, packet_data):
        #voltage_checksum = packet_data[12]
        #current_checksum = packet_data[13]
        #period_checksum = packet_data[14]
        #active_checksum = packet_data[15]
        #reactive_checksum = packet_data[16]
        #apparent_power = packet_data[17]
        #phase_angle_checksum = packet_data[18]
        #power_factor_checksum = packet_data[19]
        #checksum = packet_data[20]
        return True

    def create_packet(self, packet_data):
        flags = packet_data[2]
        epoch = packet_data[3]
        voltage = packet_data[4]* (2.37748 * 10**-4) + -0.14427
        current = packet_data[5] * (113240.82786) + 953.97194
        period = packet_data[6]
        active_power = packet_data[7]
        reactive_power = packet_data[8]
        apparent_power = packet_data[9]
        phase_angle = packet_data[10]
        power_factor = packet_data[11]
        return Packet(
            flags=flags,
            epoch=epoch,
            voltage=voltage,
            current=current,
            period=period,
            active_power=active_power,
            reactive_power=reactive_power,
            apparent_power=apparent_power,
            phase_angle=phase_angle,
            power_factor=power_factor,
        )

    def save_packets(self):
        # submit packets to lib
        if self.packet_store:
            self.listener_func(self.packet_store)
