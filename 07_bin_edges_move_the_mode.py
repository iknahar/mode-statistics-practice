import numpy as np
from listening import load_plays, hhmm
#
plays = load_plays()
for start in (6.0, 5.5):                        # on the hour, on the half
    edges = np.arange(start, 26, 1)
    counts, _ = np.histogram(plays, bins=edges)
    k = int(np.argmax(counts))
    print(hhmm(edges[k]), "to", hhmm(edges[k + 1]), counts[k], "plays")
