# Best Instrument Tuner!!!
#### Overview
We have developed an instrument tuner featuring two modes: a listening mode and a speaker mode. In listening mode, the tuner analyzes sound input from an additional microphone sensor to detect the frequency, providing feedback to users on whether they need to adjust their pitch sharper or flatter. For speaker mode, users can set the frequency of the pitch and adjust the volume using a capacitive touch sensor. Additionally, the tuner includes a metronome function, allowing users to choose from various tempos for rhythm assistance.

To help with user input for playing different notes and adjusting tempo, we have implemented a GUI. This interface includes sections displaying the frequency and notes being played, as well as a real-time display showing the current frequency detected by the tuner. Additionally, users will have access to an ideal frequency reference, allowing them to compare the detected frequency to the closest note.

In addition to the GUI for note selection and tempo adjustment, our project incorporates robust functionality to ensure accurate and responsive performance analysis. This includes signal processing algorithms such as FFT that detect and analyze the frequency of the input signal. Furthermore, the project integrates a database of ideal frequencies corresponding to standard musical notes, enabling users to compare their current frequency to the nearest note for optimal tuning accuracy.

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

#### Technical Approach
Our listening mode listens to notes, analyzes the frequency of a note, and displays the detected note and the pitch offset on a GUI display. To detect the pitch of notes, we need to select a microphone with a sampling frequency high enough to accurately capture frequencies in the 16-5000 range (frequencies of common notes). Integrating a microphone into the FRDM board involves processing the analog input into a digital value. To accomplish this, we use the microcontroller’s built-in ADC. With access to a buffer of digital values that represent the sound wave, we use the Fast Fourier Transform (FFT) to perform frequency analysis on the wave. The sound wave frequency is then compared to the frequency of the closest half-note. This half-note is then sent to the connected computer via UART and displayed on a GUI. An indicator on the display also shows whether the note is sharp or flat. 

For the speaker mode, the microcontroller will use UART to connect with serial pins on laptop to send frequency and volume to play at, and the laptop can read the information provided. It will then be connected to a python script for GUI to play the frequencies on laptop speaker.

#### Testing and Debugging
Talk about your testing approach or subtle bugs you made/found.
#### Team Work 
How did you coordinate? Who was responsible for what? You can skip this section if you work alone. 
#### Outside Resources
If you are using a code base from outside of class, or found a particular resource helpful, please put it here. 




