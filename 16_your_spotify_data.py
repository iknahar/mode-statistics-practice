import json
import sys
import numpy as np
from scipy.stats import gaussian_kde
from scipy.signal import find_peaks
from listening import hhmm
#
# usage: python 16_your_spotify_data.py StreamingHistory0.json
# works with the basic "Account data" files (endTime, trackName)
# and the "Extended streaming history" files (ts, master_metadata_...)
path = sys.argv[1] if len(sys.argv) > 1 else "sample_streaming_history.json"
rows = json.load(open(path, encoding="utf-8"))
hours, songs = [], []
for r in rows:
    stamp = r.get("endTime") or r.get("ts")       # "2026-10-01 22:31"
    clock = stamp.replace("T", " ")[11:16]        # keep "22:31"
    h, m = int(clock[:2]), int(clock[3:])
    hours.append(h + m / 60 + (24 if h < 6 else 0))   # after midnight
    songs.append(r.get("trackName") or r.get("master_metadata_track_name"))
hours = np.array(hours)
print("your mode song:", max(set(songs), key=songs.count))
print("your mean time:", hhmm(hours.mean()))
grid = np.linspace(6, 30, 1441)
h = gaussian_kde(hours)(grid)
tops, _ = find_peaks(h, prominence=h.max() * 0.05)
print("your hilltops:", [hhmm(t) for t in grid[tops]])
