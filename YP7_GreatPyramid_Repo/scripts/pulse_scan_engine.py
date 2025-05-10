# Applies skip intervals to vector data
def scan_pulse(sequence, skip):
    return [sequence[i] for i in range(0, len(sequence), skip)]
