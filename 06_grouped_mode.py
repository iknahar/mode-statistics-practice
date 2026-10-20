import numpy as np
from gym import hhmm
#
def grouped_mode(edges, counts):
    k = int(np.argmax(counts))                  # the busiest bar
    f1 = counts[k]
    f0 = counts[k - 1] if k > 0 else 0          # bar before, or nothing
    f2 = counts[k + 1] if k + 1 < len(counts) else 0
    L, h = edges[k], edges[k + 1] - edges[k]    # where it starts, how wide
    return L + (f1 - f0) / ((f1 - f0) + (f1 - f2)) * h
#
edges = np.arange(16, 22)                       # 16:00 to 21:00
counts = [49, 130, 185, 135, 55]
print(hhmm(grouped_mode(edges, counts)))
