import numpy as np
from scipy.stats import gaussian_kde
from scipy.signal import find_peaks
from gym import load_times
#
times = load_times()
grid = np.linspace(5, 23, 721)
for minutes in (3, 6, 24, 60, 84, 300):
    w = minutes / 60                               # hill width in hours
    kde = gaussian_kde(times, bw_method=w / times.std(ddof=1))
    h = kde(grid)
    tops, _ = find_peaks(h, prominence=h.max() * 0.004)
    print(minutes, "min wide:", len(tops), "hilltops")
