import numpy as np
import serial
import math
from constants import A4

class FrequencyReader:
    def __init__(self, data_points, serial):
        self.serial_connection = serial
        self.data_points = data_points
        print(f"Connected to serial.")

    def read_from_port(self):
        data = []
        while len(data) < self.data_points:
            line = self.serial_connection.readline().decode().strip()
            if line.startswith('New Reading:'):
                number = int(line.split(':')[1])
                data.append(number)
        return data

    def perform_fft(self, data):
        data_centered = data - np.mean(data)
        window = np.hanning(len(data_centered))
        data_windowed = data_centered * window
        padded_data = np.pad(data_windowed, (0, len(data_windowed)), mode='constant', constant_values=(0, 0))
        fft_result = np.fft.fft(padded_data)
        freqs = np.fft.fftfreq(len(fft_result), d=1/195000)
        mag = np.abs(fft_result)
        dominant_frequency = np.abs(freqs[np.argmax(mag)])
        return dominant_frequency

    def find_frequency(self):
        collected_data = self.read_from_port()
        if collected_data:
            return self.perform_fft(collected_data)

    def find_nearest_note(frequency):
        # Calculate C0 as the base frequency, which is the C note below the lowest A (A0)
        C0 = A4 * math.pow(2, -4.75)
        note_names = [
            'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
        ]

        if frequency < C0:
            return "Frequency too low", None, None

        half_steps_from_C0 = 12 * math.log2(frequency / C0)
        nearest_note_index = round(half_steps_from_C0)
        note = note_names[nearest_note_index % 12]
        nearest_note_frequency = C0 * math.pow(2, nearest_note_index / 12)

        deviation = frequency - nearest_note_frequency
        if abs(deviation) < 2:
            tuning_status = "In Tune"
        elif deviation < 0:
            tuning_status = "Flat"
        else:
            tuning_status = "Sharp"

        return note, nearest_note_frequency, tuning_status, deviation     