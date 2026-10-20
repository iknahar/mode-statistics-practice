import pandas as pd
#
MONTHS = {"Aug": {"Night Bus": 9, "Lo-fi Rain": 14, "Gym Hype": 6},
          "Sep": {"Night Bus": 17, "Lo-fi Rain": 8, "Gym Hype": 11},
          "Oct": {"Night Bus": 12, "Lo-fi Rain": 12, "Gym Hype": 7}}
rows = [(m, s) for m, d in MONTHS.items() for s, n in d.items()
        for _ in range(n)]                   # one row per play
df = pd.DataFrame(rows, columns=["month", "song"])
top = df.groupby("month")["song"].agg(lambda s: s.mode().tolist())
print(top)
