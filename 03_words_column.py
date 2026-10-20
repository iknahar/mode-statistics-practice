import pandas as pd
#
classes = pd.Series(["Spin"] * 41 + ["HIIT"] * 35 + ["Yoga"] * 28
                    + ["Pilates"] * 17)
print(classes.value_counts())    # the whole leaderboard
print(classes.mode()[0])         # just the winner
try:
    classes.mean()               # adding words together
except TypeError:
    print("mean: pandas refuses, good")
