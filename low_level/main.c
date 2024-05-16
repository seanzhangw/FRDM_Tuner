/* ADC Example code for ECE3140
 *
 * Nils Napp May 2023
 *
 * Based on example by Evan Greavu
 */

#include <pin_mux.h>
#include <clock_config.h>
#include <stdio.h>
#include <board.h>
#include <MKL46Z4.h>
#include <fsl_debug_console.h>

// switch
const int RED_LED_PIN = 29;
const int SWITCH_1_PIN = 3;
SIM_Type* global_SIM = SIM;
PORT_Type* global_PORTE = PORTE;
GPIO_Type* global_PTE = PTE;
PORT_Type* global_PORTC = PORTC;
GPIO_Type* global_PTC = PTC;

volatile int listenMode = 1;

void metronome();
void listen_mode();

/*
 * The macro definitions are for the setup function are in in MKL46Z4.h
 * To use, cut-n-paste this code into your project  and #include <MKL46Z4.h>
 * if it is not already included
 */
void SetupADC()
{

    int cal_v;

    // Enable clock gate for ADC0
    SIM->SCGC6 |= (1 << 27);

    // Setup ADC
    ADC0->CFG1 = 0;                      // Default everything.
    ADC0->CFG1 |= ADC_CFG1_ADICLK(0b00); // Use bus clock.
    ADC0->CFG1 |= ADC_CFG1_MODE(0b10);   // 00 for 8-bit
                                         // 01 for 12-bit
                                         // 10 for 10-bit
                                         // 11 for 16-bit

    // Calibrate
    ADC0->SC3 = 0;
    ADC0->SC3 |= ADC_SC3_AVGS(0b11); // SelectMaximum Hardware Averaging (32) see 28.3.7 for details
    ADC0->SC3 |= ADC_SC3_AVGE_MASK;  // Enable Hardware Averaging
    ADC0->SC3 |= ADC_SC3_CAL_MASK;   // Start Calibration

    // Wait for calibration to complete
    while (!(ADC0->SC1[0] & ADC_SC1_COCO_MASK))
        ;

    // Assume calibration worked, or check ADC_SC3_CALF

    // Calibration Complete, write calibration registers.
    cal_v = ADC0->CLP0 + ADC0->CLP1 + ADC0->CLP2 + ADC0->CLP3 + ADC0->CLP4 + ADC0->CLPS;
    cal_v = cal_v >> 1 | 0x8000;
    ADC0->PG = cal_v;

    cal_v = 0;
    cal_v = ADC0->CLM0 + ADC0->CLM1 + ADC0->CLM2 + ADC0->CLM3 + ADC0->CLM4 + ADC0->CLMS;
    cal_v = cal_v >> 1 | 0x8000;
    ADC0->MG = cal_v;

    ADC0->SC3 = 0; // Turn off hardware averaging for faster conversion
                   // or enable as above in calibration.
    return;
}

void operate_switch_interrupts() {
	NVIC_EnableIRQ(PORTC_PORTD_IRQn); // configure NVIC so that interrupt is enabled
}

char uart_getc(void) {
    // Wait until a character is received
    while (!(UART0->S1 & UART_S1_RDRF_MASK));
    // Read and return the received character
    return UART0->D;
}

void uart_gets(char *buffer, int max_len) {
    int i = 0;
    char c;
    while (i < max_len - 1) {
        c = uart_getc();
        if (c == '\n') {
            break;
        }
        buffer[i++] = c;
    }
    buffer[i] = '\0'; // Null terminate the string
}

void listen_mode() {
    uint16_t mic_values[4096]; // Array to store light values

	while (1)
	{
		if (!listenMode) {
			metronome();
		}
		// Loop to read light values into the array
		for (int i = 0; i < 4096; i++)
		{
			ADC0->SC1[0] = ADC_SC1_ADCH(3); // Start conversion by writing the channel
											// to ADCH. The light sensor is on channel 3

			while (!(ADC0->SC1[0] & ADC_SC1_COCO_MASK))
				; // Block until conversion is complete

			mic_values[i] = ADC0->R[0];
		}
		for (int j = 0; j < 4096; j++)
		{
			PRINTF("New Reading: %d\n\r", mic_values[j]);
		}
	}
}

void metronome() {
	char buffer[5];

	uart_gets(buffer, 5);
    int bpm = atoi(buffer);

	while (1) {
		if (listenMode) {
			listen_mode();
		}
		int j = 0;
		PTE->PTOR = GPIO_PTOR_PTTO(1 << RED_LED_PIN);
		while (j < bpm*7100) {
			j++;
		}
	}
}

void PORTC_PORTD_IRQHandler(void) {
	PORTC->PCR[SWITCH_1_PIN] |= PORT_PCR_ISF(1);  // clear the interrupt status flag by writing 1 to it
	// button pressed, toggle LED?
	listenMode ^= 1;
}


int main(void)
{
    // THIS CODE IS ONLY HERE FOR THE PRINTF
    BOARD_InitBootPins();
    BOARD_InitBootClocks();
    BOARD_InitDebugConsole();

    //^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    SetupADC();

    SIM->SCGC5 |= (1 << 13); // Enable Speaker I/O Port
                             // Pin defaults to ADC
	// setup red led
	SIM->SCGC5 |= SIM_SCGC5_PORTE_MASK; //Enable the clock to port E
	PORTE->PCR[RED_LED_PIN] = PORT_PCR_MUX(0b001); //Set up PTE29 as GPIO
	PTE->PDDR |= GPIO_PDDR_PDD(1 << RED_LED_PIN); // make it output
	PTE->PSOR |= GPIO_PSOR_PTSO(1 << RED_LED_PIN); // turn off LED

	// setup switch 1
	SIM->SCGC5 |= SIM_SCGC5_PORTC_MASK; //Enable the clock to port C
	PORTC->PCR[SWITCH_1_PIN] &= ~PORT_PCR_MUX(0b111); // Clear PCR Mux bits for PTC3
	PORTC->PCR[SWITCH_1_PIN] |= PORT_PCR_MUX(0b001); // Set up PTC3 as GPIO
	PTC->PDDR &= ~GPIO_PDDR_PDD(1 << SWITCH_1_PIN); // make it input
	PORTC->PCR[SWITCH_1_PIN] |= PORT_PCR_PE(1); // Turn on the pull enable
	PORTC->PCR[SWITCH_1_PIN] |= PORT_PCR_PS(1); // Enable the pullup resistor
	PORTC->PCR[SWITCH_1_PIN] &= ~PORT_PCR_IRQC(0b1111); // Clear IRQC bits for PTC3
	PORTC->PCR[SWITCH_1_PIN] |= PORT_PCR_IRQC(0b1010); // Set up the IRQC to interrupt on either edge (i.e. from high to low or low to high)

	operate_switch_interrupts();

	if (listenMode) {
		listen_mode();
	} else {
		metronome();
	}


    return 0;
}
