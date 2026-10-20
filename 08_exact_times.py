import numpy as np
from scipy import stats
from gym import load_times, hhmm
#
times = load_times()
print(len(times), "times,", len(np.unique(times)), "different")
res = stats.mode(times)
print("scipy's mode:", hhmm(res.mode), "seen", res.count, "time")
