# Your project ECE3140 page!

You can modify this page to create your final project page. Right now, the page is generated from a Markdown file (index.md) in the `page` branch. You can edit it directly from the git web interface or push it to the branch. There are a few [standard themes](https://pages.github.com/themes/) github provides. This one is `minimal`. If you'd like to change it, you can edit the `\_config.yml` file.

The Markdown interface is easy, but if you would like to do something different you can add an index.html file to the branch (and any supporitng style sheets etc.) and it will be served as the webpage instead. 

# Expected page structure 

We would like your final project page to have the following structure:
- A very catchy title
- An overview section about the project
- A system diagrm that shows the major hw/sw components and how they interact 
- A short video (3-4 min) that covers:
  - Who you are
  - Project title and idea
  - Technical approach
  - A demo of the working product
  - Any technical difficulties you faced or your testing/debugging approach. Think of what YOU would have liked to know BEFORE you started this project.
  - _Please keep to the 3-4min lenght since we will ask students to watch a bunch of these. If you want a longer video that goes into more detail you can add anohter one in the technical section_. 
- Technical approach (This should be more detailed than the information in the video)
- Testing / debugging aproach
- Team work (if applicable)
- Outside resrouces

## The section headings we expct to see are:

#### Overview (Fill in for web checkin May 3)
We built an instrument tuner that has two modes: a speaker and listening mode. For listening, it would take sound input and detect the frequency to tell users if they need to be sharper or flatter. An extra microphone sensor is used to take in the signal and analyze. For speaker mode, the tuner would be able to set the frequency of the pitch and the volume with the capacitive touch sensor. In addition, the board will also support a metronome function that can play at different tempo.

In order to allow input from users to play different notes and tempo, a GUI is implemented that contains the frequency and notes played, and a display that shows the current frequency listened to. There will also be an ideal frequency of the closest note to compare to.

In addition to the text, this should have the video (not needed by May 3) and the system diagram in it. You can embed an youtube video here. Please use a horizontal layout for the video if possible. 

#### Technical Approach (Fill in for web checkin May 3)
Our listening mode listens to notes, analyzes the frequency of a note, and displays the detected note and the pitch offset on a GUI display. To detect the pitch of notes, we need to select a microphone with a sampling frequency high enough to accurately capture frequencies in the 16-5000 range (frequencies of common notes). Integrating a microphone into the FRDM board involves processing the analog input into a digital value. To accomplish this, we use the microcontroller’s built-in ADC. With access to a buffer of digital values that represent the sound wave, we use the Fast Fourier Transform (FFT) to perform frequency analysis on the wave. The sound wave frequency is then compared to the frequency of the closest half-note. This half-note is then sent to the connected computer via UART and displayed on a GUI. An indicator on the display also shows whether the note is sharp or flat. 

For the speaker mode, the microcontroller will use UART to connect with serial pins on laptop to send frequency and volume to play at, and the laptop can read the information provided. It will then be connected to a python script for GUI to play the frequencies on laptop speaker

#### Testing and Debugging
Talk about your testing approach or subtle bugs you made/found.
#### Team Work 
How did you coordinate? Who was responsible for what? You can skip this section if you work alone. 
#### Outside Resources
If you are using a code base from outside of class, or found a particular resource helpful, please put it here. 




