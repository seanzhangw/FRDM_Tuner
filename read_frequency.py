import numpy as np
import serial

# Parameters
COM_PORT = 'COM3'
BAUD_RATE = 115200
DATA_POINTS = 4096  # Number of samples

# Initialize serial port
ser = serial.Serial(COM_PORT, BAUD_RATE)
print(f"Connected to {COM_PORT} at {BAUD_RATE} baud.")

def read_from_port(serial_connection):
    data = []
    while len(data) < DATA_POINTS:
        line = serial_connection.readline().decode().strip()
        if line.startswith('New Reading:'):
            number = int(line.split(':')[1])
            data.append(number)
    return data


def perform_fft(data):
    # Remove DC offset
    data_centered = data - np.mean(data)

    # Apply a window
    window = np.hanning(len(data_centered))
    data_windowed = data_centered * window

    # Zero-padding
    padded_data = np.pad(data_windowed, (0, len(data_windowed)), mode='constant', constant_values=(0, 0))

    # Perform FFT
    fft_result = np.fft.fft(padded_data)
    freqs = np.fft.fftfreq(len(fft_result), d=1/190000)  # Adjust 'd' as per your actual sampling interval

    # Find the magnitude and corresponding frequency
    mag = np.abs(fft_result)

    dominant_frequency = np.abs(freqs[np.argmax(mag)])

    print(f"Dominant Frequency: {dominant_frequency} Hz")
    return dominant_frequency

def find_frequency():
    collected_data = read_from_port(ser)
    if collected_data:
        dominant_freq = perform_fft(collected_data)
    return dominant_freq
        
while True:
    try:
        find_frequency()
    except KeyboardInterrupt:
        print("Stopped")
        break
    except :
        continue

