import math

def find_nearest_note(frequency):
    # Define A4 as the reference point
    A4 = 440
    # Calculate C0 as the base frequency, which is the C note below the lowest A (A0)
    C0 = A4 * math.pow(2, -4.75)
    note_names = [
        'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    ]

    if frequency < C0:
        return "Frequency too low", None, None

    # Calculate how many half-steps the frequency is from C0
    half_steps_from_C0 = 12 * math.log2(frequency / C0)
    # Round to the nearest whole number to find the closest note
    nearest_note_index = round(half_steps_from_C0)
    # Use modulo to wrap around the note_names list
    note = note_names[nearest_note_index % 12]
    
    # Calculate the exact frequency of the nearest note
    nearest_note_frequency = C0 * math.pow(2, nearest_note_index / 12)

    # Determine the deviation from the exact frequency
    deviation = frequency - nearest_note_frequency
    if abs(deviation) < 1:
        tuning_status = "In Tune"
    elif deviation < 0:
        tuning_status = "Flat"
    else:
        tuning_status = "Sharp"

    return note, nearest_note_frequency, tuning_status

# Example usage
frequency = 453
note, note_frequency, status = find_nearest_note(frequency)
print(f"The frequency {frequency} Hz is closest to {note} ({note_frequency:.2f} Hz) and is {status}.")
