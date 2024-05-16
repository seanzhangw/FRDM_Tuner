import tkinter as tk
from components.FrequencyReader import FrequencyReader
from components.Gui import GUI
import FrequencyProcessor as fp
from constants import COM_PORT, BAUD_RATE, DATA_POINTS
import threading
import serial
import time

class TunerApp:
    def __init__(self) -> None:
        serial_connection = serial.Serial(COM_PORT, BAUD_RATE)
        reader = FrequencyReader(DATA_POINTS, serial_connection)
        root = tk.Tk()
        app = GUI(root, serial_connection)
        self.start_frequency_reading(reader, app, 1000)
        root.mainloop()

    def start_frequency_reading(self, reader, app, interval):
        def thread_target():
            while True:
                try:
                    frequency = reader.find_frequency() - 30
                    note, nearest_freq, status, deviation = FrequencyReader.find_nearest_note(frequency)
                    print(note, nearest_freq, status, deviation)
                    # Update GUI safely from another thread
                    app.master.after(0, app.update_display, note, status == 'Flat', status == 'Sharp', deviation)
                except Exception as e:
                    print(e)
                time.sleep(interval / 1000)  
        
        threading.Thread(target=thread_target, daemon=True).start()
