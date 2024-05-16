# Best Instrument Tuner!!!
#### Overview
We have developed an instrument tuner featuring two modes: a listening mode and a metronome mode. In listening mode, the tuner analyzes sound input from an additional microphone sensor to detect the frequency, providing feedback to users on whether they need to adjust their pitch sharper or flatter. For metronome mode, users can set a beat per minute (bpm), and the red LED on the board will flash at the same speed, allowing users to visualize their tempo for rhythm assistance.

To help with user input for playing different notes and adjusting tempo, we have implemented a GUI. This interface includes sections displaying the notes being played, whether the note is in tune or not, and an input label for BPM. Additionally, a progress bar has been integrated, providing real-time feedback on the proximity of the played note to the desired pitch, enabling users to fine-tune their intonation.

In addition to the GUI for note selection and tempo adjustment, our project incorporates signal processing algorithms such as FFT that detect and analyze the frequency of the input signal. Furthermore, the project integrates a database of ideal frequencies corresponding to standard musical notes, enabling users to compare their current frequency to the nearest note for optimal tuning accuracy.

![Alt text for the diagram](/system_diagram.png)

#### Technical Approach
Our listening mode serves as the core functionality of our project, providing real-time analysis of played notes and delivering feedback to users. This mode begins by capturing audio input through a microphone sensor with a high sampling frequency sufficient to capture frequencies within the 16-5000 Hz range, covering common musical notes. Integration of the microphone into the FRDM board involves processing the analog input into digital values using the microcontroller's built-in ADC (Analog-to-Digital Converter).

Once the audio waveform is digitized with values representing the sound wave, we utilize the Fast Fourier Transform (FFT) algorithm to perform frequency analysis on the signal. The detected frequency is then compared to the frequencies of nearby half-notes, allowing us to identify the closest musical note to the played frequency. The results of this analysis are sent to the connected computer via UART and displayed on a GUI. Users can view the whether the note is sharp or flat, with an indicator on the GUI display to inform users whether the detected note is sharp or flat.

In metronome mode, our project uses UART communication to establish a connection between the microcontroller and a computer. Through UART, the computer sends information about the desired bpm to the to the microcontroller. The microcontroller, in turn, reads this information and initiates the necessary actions to generate the specified bpm. To help with this process, a Python script is utilized on the laptop side. This script interfaces with the serial pins to send the bpm data set by users to the microcontroller in the format of chars, sending each digit of the bpm one by one. 

After the bpm value is received, each digit of the char is combined and converted to integers. A while loop is called which will first toggle the red LED, wait for 60/bpm seconds, and toggle the red LED again to flash the LED at the desired bpm. 

To incorporate both the listening and metronome mode, switch 1 is utilized through interrupts. If switch 1 is pressed, it will trigger an interrupt that stops all the actions, and the microcontroller will switch the mode from listening to metronome, or vice versa.

#### Testing and Debugging

There are multiple errors encountered during implementation. For instance, initially implemented the code in a way that calls the helper method to listening mode and metronome inside the IRQ handler. Both the helper methods for listening mode and metronome include infinite while loops, and when interrupts are disabled inside IRQ handler, the while loops get stuck and it wouldn't transition into a different mode when the switch is pressed. We figured out the error by writing print statements that let us know where the processor is at, and therefore we found out that the processor is stuck in an infinite while loop even when interrupts are triggered.

At first we are confused since interrupts will stop while, save the stack pointer and perform ISR, and return to the while loop. However, after careful debug we found out that helper methods are called in IRQ handler. To resolve the issue, we added if statements inside each helper method that will connect to the other method when there is a switch.


#### Team Work 
We distributed work evenly, where all the coding was done collaboratively, by meetup. When coding was complete, we worked collaboratively on the website together. For the testing section, we each contributed ideas and possible errors in our code.

#### Outside Resources
No outside resources are used.




