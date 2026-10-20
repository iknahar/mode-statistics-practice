import numpy as np
from scipy.stats import norm
from scipy.signal import find_peaks
#
x = np.linspace(-6, 10, 4001)
for gap in (1.0, 1.5, 1.9, 2.0, 2.1, 3.0):
    y = 0.5 * norm.pdf(x, 0, 1) + 0.5 * norm.pdf(x, gap, 1)
    print("gap", gap, "sd ->", len(find_peaks(y)[0]), "hill(s)")
