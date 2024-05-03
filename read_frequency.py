import serial
import numpy as np
import time

# Parameters
COM_PORT = 'COM3'  # COM port (adjust as necessary)
BAUD_RATE = 115200  # Baud rate
DATA_POINTS = 4000  # Number of data points for FFT

# Initialize serial port
ser = serial.Serial(COM_PORT, BAUD_RATE)
print(f"Connected to {COM_PORT} at {BAUD_RATE} baud.")

def read_from_port(serial_connection):
    """Read lines from the serial port and perform FFT."""
    data = []
    try:
        while len(data) < DATA_POINTS:
            if serial_connection.in_waiting > 0:
                line = serial_connection.readline().decode('utf-8', 'ignore').strip()
                # Extract the numeric value from the line
                if line.startswith('New Reading:'):
                    number = int(line.split(':')[1].strip())
                    data.append(number)
    except KeyboardInterrupt:
        print("Stopped by user.")
    
    return data

def perform_fft(data):
    print("data: " + str(data))
    """Perform FFT on the collected data and find the dominant frequency."""

    data_center = data - np.mean(data)
    # Perform FFT
    fft_result = np.fft.fft(data_center)
    freqs = np.fft.fftfreq(len(fft_result))
    # Find the magnitude
    mag = np.abs(fft_result)
    
    # Frequency resolution
    sample_rate = 189000
    dominant_frequency = np.abs(freqs[np.argmax(mag)]) * sample_rate
    
    print(f"Dominant Frequency: {dominant_frequency} Hz")
    return dominant_frequency

try:
    start_time = time.time()
    collected_data = read_from_port(ser)
    dominant_freq = perform_fft(collected_data)
finally:
    ser.close()
    print("Serial port closed.")
