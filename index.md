# Best Instrument Tuner!!!
#### Overview
We have developed an instrument tuner featuring two modes: a listening mode and a speaker mode. In listening mode, the tuner analyzes sound input from an additional microphone sensor to detect the frequency, providing feedback to users on whether they need to adjust their pitch sharper or flatter. For speaker mode, users can set the frequency of the pitch and adjust the volume using a capacitive touch sensor. Additionally, the tuner includes a metronome function, allowing users to choose from various tempos for rhythm assistance.

To help with user input for playing different notes and adjusting tempo, we have implemented a GUI. This interface includes sections displaying the frequency and notes being played, as well as a real-time display showing the current frequency detected by the tuner. Additionally, users will have access to an ideal frequency reference, allowing them to compare the detected frequency to the closest note.

In addition to the GUI for note selection and tempo adjustment, our project incorporates signal processing algorithms such as FFT that detect and analyze the frequency of the input signal. Furthermore, the project integrates a database of ideal frequencies corresponding to standard musical notes, enabling users to compare their current frequency to the nearest note for optimal tuning accuracy.

![Alt text for the diagram](/system_diagram.png)

#### Technical Approach
Our listening mode serves as the core functionality of our project, providing real-time analysis of played notes and delivering feedback to users. This mode begins by capturing audio input through a microphone sensor with a high sampling frequency sufficient to capture frequencies within the 16-5000 Hz range, covering common musical notes. Integration of the microphone into the FRDM board involves processing the analog input into digital values using the microcontroller's built-in ADC (Analog-to-Digital Converter).

Once the audio waveform is digitized with values representing the sound wave, we utilize the Fast Fourier Transform (FFT) algorithm to perform frequency analysis on the signal. The detected frequency is then compared to the frequencies of nearby half-notes, allowing us to identify the closest musical note to the played frequency. The results of this analysis are sent to the connected computer via UART and displayed on a GUI. Users can view the frequency of the detected note, with an indicator on the GUI display to inform users whether the detected note is sharp or flat.

In speaker mode, our project uses UART communication to establish a connection between the microcontroller and a computer. Through UART, the microcontroller sends information about the desired frequency and volume levels to the serial pins on the laptop. The laptop, in turn, reads this information and initiates the necessary actions to generate the specified frequencies and control the volume.

To help with this process, a Python script is utilized on the laptop side. This script interfaces with the serial pins to receive the frequency and volume data transmitted by the microcontroller. Additionally, the Python script generates audio output based on the received frequency information. This output is then played through the laptop's speaker, providing users with audible feedback corresponding to the desired frequency and volume settings.

#### Testing and Debugging
Talk about your testing approach or subtle bugs you made/found.
#### Team Work 
How did you coordinate? Who was responsible for what? You can skip this section if you work alone. 
#### Outside Resources
If you are using a code base from outside of class, or found a particular resource helpful, please put it here. 




