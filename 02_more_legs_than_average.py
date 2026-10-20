import numpy as np
#
legs = np.array([2] * 98 + [1] * 2)      # 100 people, two with one leg
print("mean legs:", legs.mean())
print("mode:", np.bincount(legs).argmax())
print("people above the mean:", (legs > legs.mean()).sum())
