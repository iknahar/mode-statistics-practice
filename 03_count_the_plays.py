from collections import Counter
#
last20 = (["Night Bus"] * 7 + ["Lo-fi Rain"] * 5 + ["Gym Hype"] * 4
          + ["Sad Song 4"] * 2 + ["Ad Jingle"] * 2)
tally = Counter(last20)          # song -> how many plays
print(tally.most_common(2))      # the winner and the runner-up
