import statistics
import pandas as pd
from scipy import stats
#
songs = ["Night Bus", "Lo-fi Rain", "Night Bus", "Gym Hype", "Lo-fi Rain",
         "Ad Jingle"]
print(statistics.mode(songs))             # the first winner it met
print(statistics.multimode(songs))        # every winner, in order met
print(pd.Series(songs).mode().tolist())   # every winner, sorted A to Z
try:
    stats.mode(songs)                     # scipy only takes numbers
except TypeError:
    print("scipy: numbers only, please")
#
# old tutorials wrote stats.mode(x)[0][0], which breaks on SciPy 1.11+
res = stats.mode([3, 1, 3, 2])
print(res.mode, res.count)                # read the parts by name
