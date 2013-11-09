/*
 * HAL_SPI.c
 *
 * Created: 11/8/2013 8:03:16 PM
 *  Author: DJD103
 *
 * VFD_MOSI - PB1, pin 20
 * VFD_BUSY - PA4/PGMN0, pin 77
 * VFD_SCK - PB13, pin 144
 * VFD_NRST - PC28, pin 76
 */ 

#include "sam.h"
#include <stdint.h>

// Call this in the setup, not main loop of the firmware
void sam_uart_spi_init(){
	
	
	
	/* Below, UART-SPI config for the VFD */
	
	// MOSI aka PB1 must be output
	// BUSY aka PA4/PGMN0 must be input
	// SCK aka PB13 must be output
	// NRST aka PC28 must be output
	
	//value programmed in cd must be >= 6
	
	// CPOL must be 0
	// CPHA must be... 
	
	//generate SCK freq of 2 MHz from 120 MHz sysclk
	
	// disable write protect via WPMR register?
	US_MR = 0xE; //initialize usart in SPI master mode - write 0xE to USART_MODE field in mode reg
	
	// see p. 853 in datasheet
	// MOSI is driven by TXD, MISO by RXD, SCK SCK and NSS RTS pin
	// 
}

void hal_spi_chip_select(){
	// bring CS pin low
	// PIO Controller talked about on p.657
	// AFE CS is PC4, pin 41, D4 peripheal A
}

void hal_spi_chip_deselect(){
	// bring CS pin high
	// just invert code in above function
}

void hal_spi_write_byte(uint8_t towrite)
{
	// write towrite to the register
	// look into the Transmit Holding Register (US_THR)
	// have a busy loop
}

