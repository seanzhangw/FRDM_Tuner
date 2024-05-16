import math
from constants import A4

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