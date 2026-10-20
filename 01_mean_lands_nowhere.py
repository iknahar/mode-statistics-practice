import numpy as np
from gym import load_times, hhmm
#
times = load_times()
print("mean check-in:", hhmm(times.mean()))
counts, edges = np.histogram(times, bins=np.arange(5, 24))
print("people in the 13:00 hour:", counts[13 - 5])
print("people in the 18:00 hour:", counts[18 - 5])
