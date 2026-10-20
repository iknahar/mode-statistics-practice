import numpy as np
from scipy.stats import gaussian_kde
from scipy.signal import find_peaks
from listening import load_plays, hhmm
#
plays = load_plays()
curve = gaussian_kde(plays)            # a small hill on every play
grid = np.linspace(6, 25, 1901)        # a point every 36 seconds
height = curve(grid)
tops, _ = find_peaks(height)           # higher than both neighbours
print([hhmm(t) for t in grid[tops]])
