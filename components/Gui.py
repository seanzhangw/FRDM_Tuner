from tkinter import ttk
import random
import tkinter as tk
import serial  

class GUI:
    def __init__(self, master, serial):
        self.master = master
        self.serial_connection = serial
        master.title("Tuner")

        # Note display
        self.note_label = ttk.Label(master, text="Note: ", font=('Helvetica', 16))
        self.note_label.pack(pady=10)

        # Tuning display
        self.tuning_label = ttk.Label(master, text="In Tune", font=('Helvetica', 16))
        self.tuning_label.pack(pady=10)

        # Progress bar for tuning indicator
        self.progress_bar = ttk.Progressbar(master, length=200, mode='determinate')
        self.progress_bar.pack(pady=20)

        # BPM entry
        self.bpm_label = ttk.Label(master, text="Enter BPM:", font=('Helvetica', 12))
        self.bpm_label.pack(pady=5)

        self.bpm_entry = ttk.Entry(master)
        self.bpm_entry.pack(pady=5)

        self.bpm_button = ttk.Button(master, text="Set BPM", command=self.set_bpm)
        self.bpm_button.pack(pady=5)

    def update_display(self, note, is_flat, is_sharp, deviation):
        """Updates the labels and the progress bar based on the current note and its tuning."""
        self.note_label.config(text=f"Note: {note}")
        if is_flat:
            self.tuning_label.config(text="Flat")
        elif is_sharp:
            self.tuning_label.config(text="Sharp")
        else:
            self.tuning_label.config(text="In Tune")
        
        # Update progress bar
        self.progress_bar['value'] = 50 + deviation  # Adjust the range to 0-100 for the progress bar

    def simulate_note(self):
        """Simulates detecting a note; replace with actual detection logic."""
        notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        note = random.choice(notes)
        deviation = random.randint(-50, 50)
        self.update_display(note, deviation < 0, deviation > 0, deviation)

    def set_bpm(self):
        """Handles setting the BPM from user input."""
        bpm = self.bpm_entry.get()
        try:
            bpm = int(bpm)  # Convert the value to an integer
            self.serial_connection.write(b'60\n')
            print("Set bpm to " + str(bpm))
        except ValueError:
            print("Please enter a valid number")  # Handle the case where input is not a valid integer

# Creating the main window and passing it to the GUI class
if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
