# Best Instrument Tuner!!!
#### Overview
We have developed an instrument tuner featuring two modes: a listening mode and a metronome mode. In listening mode, the tuner analyzes sound input from an additional microphone sensor to detect the frequency, providing feedback to users on whether they need to adjust their pitch sharper or flatter. For metronome mode, users can set a beat per minute (bpm), and the red LED on the board will flash at the same speed, allowing users to visualize their tempo for rhythm assistance.

To help with user input for playing different notes and adjusting tempo, we have implemented a GUI. This interface includes sections displaying the notes being played, whether the note is in tune or not, and an input label for BPM. Additionally, a progress bar has been integrated, providing real-time feedback on the proximity of the played note to the desired pitch, enabling users to fine-tune their intonation.

In addition to the GUI for note selection and tempo adjustment, our project incorporates signal processing algorithms such as FFT that detect and analyze the frequency of the input signal. Furthermore, the project integrates a database of ideal frequencies corresponding to standard musical notes, enabling users to compare their current frequency to the nearest note for optimal tuning accuracy.

### System Diagram
![Alt text for the diagram](/tunerdiagramv2.drawio.png)

### Video


#### Technical Approach
Our listening mode serves as the core functionality of our project, providing real-time analysis of played notes and delivering feedback to users. This mode begins by capturing audio input through a microphone sensor with a high sampling frequency sufficient to capture frequencies within the 16-5000 Hz range, covering common musical notes. Integration of the microphone into the FRDM board involves processing the analog input into digital values using the microcontroller's built-in ADC (Analog-to-Digital Converter).

Once the audio waveform is digitized with values representing the sound wave, we utilize the Fast Fourier Transform (FFT) algorithm to perform frequency analysis on the signal. The detected frequency is then compared to the frequencies of nearby half-notes, allowing us to identify the closest musical note to the played frequency. The results of this analysis are sent to the connected computer via UART and displayed on a GUI. Users can view the whether the note is sharp or flat, with an indicator on the GUI display to inform users whether the detected note is sharp or flat.

In metronome mode, our project uses UART communication to establish a connection between the microcontroller and a computer. Through UART, the computer transmits information regarding the desired beats per minute (bpm) to the microcontroller. Upon receiving this data, the microcontroller interprets it and triggers the required operations to generate the specified bpm. To help with this process, a Python script is utilized on the laptop side. This script interfaces with the serial pins, transmitting the bpm data set by users to the microcontroller in character format, with each digit of the bpm being sent individually.

Once the bpm value is received, each character representing a digit is combined and converted into integers. A while loop is used, initiating the toggling of the red LED. It then waits for 60/bpm seconds before toggling the red LED again, thereby creating a flashing effect at the desired bpm.

Incorporating both the listening and metronome modes involves utilizing switch 1 through interrupts. When switch 1 is pressed, it triggers an interrupt that halts all ongoing actions. The microcontroller then switches the mode from listening to metronome, or vice versa, based on the current mode.

#### Testing and Debugging

As we achieved incremental functionality, we thoroughly tested the additional functionality. 

Upon integrating the speaker with the FRDM_KL46Z board and observing the analog-to-digital converted output, we ensured that the digital outputs correctly represented the frequency of the environmental sound. We played a 400Hz test tone, and plotted the values to ensure the digital outputs corresponded to a 400Hz sound wave. 

Our FFT frequency analysis was tested with by observing the dominant frequency returned for various test tones. We used appropriate test tones to represent the desired frequency range we wanted to determine.

Testing our LED metronome involved sending via UART a range of BPM values and observing that the correct LED toggle rate was being set. We created a separate test script in Python to expedite this testing process.

Our mode-switching functionality was tested by invoking the interrupt handler in all possible program states.

During implementation, we encountered various errors. Initially, we structured the code to invoke helper methods for listening mode and metronome within the IRQ handler. However, both helper methods featured infinite while loops. As a result, when interrupts were disabled within the IRQ handler, these loops caused the processor to become trapped, preventing  mode transitions when switch is activated. By strategically placing print statements, we pinpointed the issue: the processor remained stuck in an infinite loop despite interrupts being triggered.

Initially, we are confused as interrupts typically halt execution of the while loop, save the stack pointer, execute the ISR, and then return to the while loop. However, through careful debugging, we identified that helper methods were being invoked directly within the IRQ handler. To address this, we introduced if statements within each helper method. These statements help with switching between methods when a switch is detected, thus resolving the issue and ensuring operation of the program.

#### Team Work 
We distributed work evenly, where all the coding was done collaboratively, by meetup. When coding was complete, we worked collaboratively on the website together. For the testing section, we each contributed ideas and possible errors in our code.

#### Outside Resources
No outside resources are used.
A microphone sensor is used for the listening mode.
