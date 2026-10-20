import numpy as np
from listening import load_plays, hhmm
#
plays = load_plays()
print("mean play time:", hhmm(plays.mean()))
counts, edges = np.histogram(plays, bins=np.arange(6, 26))
print("plays in the 16:00 hour:", counts[16 - 6])
print("plays in the 22:00 hour:", counts[22 - 6])
