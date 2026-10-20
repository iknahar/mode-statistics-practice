import numpy as np
from scipy.stats import gaussian_kde
from scipy.signal import find_peaks
from gym import load_times, hhmm
#
times = load_times()
kde = gaussian_kde(times)              # one small hill per check-in
grid = np.linspace(5, 23, 1801)        # a point every 36 seconds
height = kde(grid)
tops, _ = find_peaks(height)           # higher than both neighbours
print([hhmm(t) for t in grid[tops]])
