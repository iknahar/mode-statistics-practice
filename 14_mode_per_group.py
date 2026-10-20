import pandas as pd
#
BRANCH = {"North": {"Spin": 18, "Yoga": 9, "HIIT": 9, "Pilates": 6},
          "South": {"Spin": 11, "Yoga": 15, "HIIT": 14, "Pilates": 8},
          "Campus": {"Spin": 12, "Yoga": 4, "HIIT": 12, "Pilates": 3}}
rows = [(b, c) for b, d in BRANCH.items() for c, n in d.items()
        for _ in range(n)]
df = pd.DataFrame(rows, columns=["branch", "cls"])
fav = df.groupby("branch")["cls"].agg(lambda s: s.mode().tolist())
print(fav)
