from collections import Counter
#
picks = [10, 12, 8, 12, 15, 12, 10, 20, 12, 8, 10, 12, 15, 10, 12]
counts = Counter(picks)          # weight -> how many times it was picked
print(counts.most_common(2))     # the two biggest piles
