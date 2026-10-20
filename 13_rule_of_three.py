import numpy as np
#
rng = np.random.default_rng(3)
waits = rng.gamma(2.5, 3.0, 5000)      # minutes waiting for the squat rack
mean, median = waits.mean(), np.median(waits)
print("mean", round(mean, 2), "median", round(median, 2))
print("Pearson's guess for the mode:", round(3 * median - 2 * mean, 2))
print("true mode of this shape: 4.5")
