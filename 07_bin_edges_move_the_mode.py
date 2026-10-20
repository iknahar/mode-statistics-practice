import numpy as np
from gym import load_times, hhmm
#
times = load_times()
for start in (5.0, 4.5):                        # on the hour, on the half
    edges = np.arange(start, 24, 1)
    counts, _ = np.histogram(times, bins=edges)
    k = int(np.argmax(counts))
    print(hhmm(edges[k]), "to", hhmm(edges[k + 1]), counts[k])
