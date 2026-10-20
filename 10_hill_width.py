import numpy as np
from scipy.stats import gaussian_kde
from scipy.signal import find_peaks
from listening import load_plays
#
plays = load_plays()
grid = np.linspace(6, 25, 761)
for minutes in (3, 6, 24, 60, 107, 360):
    w = minutes / 60                               # hill width in hours
    curve = gaussian_kde(plays, bw_method=w / plays.std(ddof=1))
    h = curve(grid)
    tops, _ = find_peaks(h, prominence=h.max() * 0.004)
    print(minutes, "min wide:", len(tops), "hilltops")
