import numpy as np
from scipy import stats
from listening import load_plays, hhmm
#
plays = load_plays()
print(len(plays), "plays,", len(np.unique(plays)), "different times")
res = stats.mode(plays)
print("scipy's mode:", hhmm(res.mode), "seen", res.count, "time")
