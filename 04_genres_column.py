import pandas as pd
#
genres = pd.Series(["Pop"] * 38 + ["Lo-fi"] * 31 + ["Hip-hop"] * 22
                   + ["K-pop"] * 17 + ["Metal"] * 6)
print(genres.value_counts())     # the whole leaderboard
print(genres.mode()[0])          # just the winner
try:
    genres.mean()                # averaging words
except TypeError:
    print("mean: pandas says no")
