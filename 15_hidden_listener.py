import numpy as np
from sklearn.mixture import GaussianMixture
from listening import hhmm
#
# the month my cousin stayed: my two habits plus someone else's
rng = np.random.default_rng(8)
me = np.concatenate([rng.normal(8.0, 0.4, 330), rng.normal(22.5, 0.75, 470),
                     rng.uniform(10, 20, 60)])
kid = rng.normal(16.6, 0.5, 220)
plays = np.concatenate([me, kid])
plays = plays[(plays >= 6) & (plays < 25)]
X = plays.reshape(-1, 1)                         # sklearn wants a column
for k in (1, 2, 3, 4):
    gm = GaussianMixture(n_components=k, random_state=0).fit(X)
    print(k, "group(s), score =", round(gm.bic(X)))   # lower is better
best = GaussianMixture(n_components=3, random_state=0).fit(X)
order = np.argsort(best.means_.ravel())
for w, m in zip(best.weights_[order], best.means_.ravel()[order]):
    print(f"{w:.0%} of plays around {hhmm(m)}")
