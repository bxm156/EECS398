/*
 * NoritakeLibrary.c
 *
 * Created: 11/6/2013 1:51:18 AM
 *  Author: DJD103
 */ 

#include "sam.h"
#include "Noritake_VFD_GU7000.h"

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

int function(void)
{
    //TODO:: Please write your application code
    
    return 0;
}

void Noritake_VFD_GU7000_reset() {
	hardReset(); // this is defined in a header file you haven't included yet
}