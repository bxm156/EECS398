/*
Wattr Project: Arduino Simulation device
by Bryan Marty
*/

typedef struct Reading {
	uint32_t epoch;				// Unix Epoch of time
	uint32_t voltage;				// ADE7753_REGISTER_VRMS
	uint32_t current;				// ADE7753_REGISTER_IRMS
	uint32_t period;				// ADE7753_REGISTER_PERIOD
	uint32_t active_power;		// ADE7753_REGISTER_RAENERGY
	uint32_t reactive_power;		// ADE7753_REGISTER_LVARENERGY
	uint32_t apparent_power;		// ADE7753_REGISTER_LVAENERGY
	uint32_t phase_angle;			// TODO: Calculation
	uint32_t power_factor;			// TODO: Calculation
	
	uint8_t voltage_checksum;
	uint8_t current_checksum;
	uint8_t frequency_checksum;
	uint8_t active_power_checksum;
	
	uint8_t reactive_power_checksum;
	uint8_t apparent_power_checksum;
	uint8_t phase_angle_checksum;
	uint8_t power_factor_checksum;
} Reading;


typedef struct Packet {
	uint8_t		header;
	uint8_t		reserved;
	uint16_t	flags;
	
	Reading		payload;
	
	uint32_t	checksum;
	uint32_t	footer;
} Packet;

int timestamp;

void setup()                    // run once, when the sketch starts
{
  Serial.begin(9600);
  Serial.flush();
  timestamp = 0;
}

void print_uint32(uint32_t data)
{
  Serial.write(data);
  Serial.write(data>>8);
  Serial.write(data>>16);
  Serial.write(data>>24);
}
void print_uint16(uint32_t data)
{
  Serial.write(data);
  Serial.write(data>>8);
}
void loop()
{
  Packet p;
  p.header = 0x59;
  p.reserved = 0;
  p.flags = 0x01;
  p.payload.epoch = timestamp++;
  p.payload.voltage = 120;
  p.checksum = 0;
  p.footer = 0x5254464d;
  Serial.write(p.header);
  Serial.write(p.reserved);
  print_uint16(p.flags);
  print_uint32(p.payload.epoch);
  print_uint32(p.payload.voltage);
  print_uint32(p.payload.current);
  print_uint32(p.payload.period);
  print_uint32(p.payload.active_power);
  print_uint32(p.payload.reactive_power);
  print_uint32(p.payload.apparent_power);
  print_uint32(p.payload.phase_angle);
  print_uint32(p.payload.power_factor);
  Serial.write(p.payload.voltage_checksum);
  Serial.write(p.payload.current_checksum);
  Serial.write(p.payload.frequency_checksum);
  Serial.write(p.payload.active_power_checksum);
  Serial.write(p.payload.reactive_power_checksum);
  Serial.write(p.payload.apparent_power_checksum);
  Serial.write(p.payload.phase_angle_checksum);
  Serial.write(p.payload.power_factor_checksum);
  print_uint32(p.checksum);
  print_uint32(p.footer);
}




