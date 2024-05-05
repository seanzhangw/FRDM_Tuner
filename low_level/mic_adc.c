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

int main(void)
{

    // THIS CODE IS ONLY HERE FOR THE PRINTF
    BOARD_InitBootPins();
    BOARD_InitBootClocks();
    BOARD_InitDebugConsole();

    //^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    SetupADC();

    SIM->SCGC5 |= (1 << 13); // Enable Light Sensor I/O Port
                             // Pin defaults to ADC

    uint16_t mic_values[4096]; // Array to store light values
    while (1)
    {
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
    return 0;
}