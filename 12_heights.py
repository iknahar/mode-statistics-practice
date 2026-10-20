import numpy as np
from scipy.stats import norm
from scipy.signal import find_peaks
#
# NHANES III adults aged 20 to 29, as used by Schilling et al. (2002)
women, men = 64.1 * 2.54, 69.3 * 2.54          # inches to cm
sd_w, sd_m = 2.75 * 2.54, 2.92 * 2.54
x = np.linspace(130, 215, 4001)
y = 0.5 * norm.pdf(x, women, sd_w) + 0.5 * norm.pdf(x, men, sd_m)
print("gap:", round(men - women, 1), "cm")
print("hills:", len(find_peaks(y)[0]))
