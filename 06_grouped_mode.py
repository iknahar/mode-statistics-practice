import numpy as np
from listening import hhmm
#
def grouped_mode(edges, counts):
    k = int(np.argmax(counts))                  # the busiest bar
    f1 = counts[k]
    f0 = counts[k - 1] if k > 0 else 0          # bar before, or nothing
    f2 = counts[k + 1] if k + 1 < len(counts) else 0
    L, h = edges[k], edges[k + 1] - edges[k]    # where it starts, how wide
    return L + (f1 - f0) / ((f1 - f0) + (f1 - f2)) * h
#
edges = np.arange(20, 26)                       # 20:00 to 01:00
counts = [12, 92, 244, 121, 11]
print(hhmm(grouped_mode(edges, counts)))
