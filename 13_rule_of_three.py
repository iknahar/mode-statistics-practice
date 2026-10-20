import numpy as np
#
rng = np.random.default_rng(3)
sessions = rng.gamma(2.5, 6.0, 5000)   # minutes per listening session
mean, median = sessions.mean(), np.median(sessions)
print("mean", round(mean, 2), "median", round(median, 2))
print("Pearson's guess for the mode:", round(3 * median - 2 * mean, 2))
print("true mode of this shape: 9.0")
