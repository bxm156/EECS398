/*
 * HAL_SPI.c
 *
 * Created: 11/6/2013 1:51:18 AM
 *  Author: DJD103
 */ 

#include "sam.h"
#include "Noritake_VFD_GU7000.h"

//IGNORE THIS STUFF FOR NOW
/*
#define F_CPU							//TODO: CLOCK FREQUENCY HERE
#define NORITAKE_VFD_RESET_DELAY 500	//value is in millisec.
#define NORITAKE_VFD_HEIGHT				//TODO: FIND HEIGHT IN CHARACTERS
#define NORITAKE_VFD_WIDTH				//TODO: FIND WIDTH IN CHARACTERS
#define NORITAKE_VFD_MODEL_CLASS 7003
#define NORITAKE_VFD_GENERATION 0

#define NORITAKE_VFD_INTERFACE		//0 for serial interface
#define NORITAKE_VFD_SERIAL_SYNC 0	//0 FOR ASYNC SERIAL
#define NORITAKE_VFD_RS232 0		//0 IF MODEL ENDS IN 7003
#define NORITAKE_VFD_BAUD 115200	//VALUE IS IN BPS
#define OUT_PORT					//serial data SIN port
#define OUT_PIN						//serial data 
#define BUSY_PORT					//serial SBUSY port
#define BUSY_PIN					//serial SBUSY pin
#define RESET_PORT					//serial RESET port
#define RESET_PIN					//serial RESET pin
*/

//Toggle Chip Select
void chip_select() {
	// define all registers above
	// initialize USART to operate in SPI master mode by writing 0xE to USART_MODE field in the Mode register. 
	// see p.853 in the datasheet
	// MOSI is driven by TXD, MISO RXD, SCK SCK, NSS RTS pin.
	// see p.830 for baud rate generation
	// Set CLKO bit to 1 in mode register US_MR
	// value programmed in CD must be >= 6
	// see p.853 for other comments
	// !!!MSB always sent first in SPI mode!
	//
}

// Untoggle Chip Select

// Write byte
void write_byte(uint_8 towrite) {
	//see p.856
	// characters are sent by writing in the Transmit Holding Register (US_THR)
}


int function(void)
{
    //TODO:: Please write your application code
    
    return 0;
}

void Noritake_VFD_GU7000_reset() {
	hardReset(); // this is defined in a header file you haven't included yet
}