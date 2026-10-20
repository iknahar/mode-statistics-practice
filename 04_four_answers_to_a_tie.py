import statistics
import pandas as pd
from scipy import stats
#
data = [12, 10, 12, 15, 10, 8]
print(statistics.mode(data))             # first winner it met
print(statistics.multimode(data))        # every winner, in order met
print(pd.Series(data).mode().tolist())   # every winner, sorted
print(stats.mode(data).mode)             # one winner only
