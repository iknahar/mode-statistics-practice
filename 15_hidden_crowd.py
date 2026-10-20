import numpy as np
from sklearn.mixture import GaussianMixture
#
rng = np.random.default_rng(8)
mins = np.concatenate([rng.normal(33, 6, 240),     # class bookers
                       rng.normal(78, 12, 360)])   # lifters
X = mins.reshape(-1, 1)                            # sklearn wants a column
for k in (1, 2, 3):
    gm = GaussianMixture(n_components=k, random_state=0).fit(X)
    print(k, "crowd(s), BIC =", round(gm.bic(X)))
best = GaussianMixture(n_components=2, random_state=0).fit(X)
order = np.argsort(best.means_.ravel())          # shortest crowd first
print("shares:", best.weights_[order].round(2))
print("centres:", best.means_.ravel()[order].round(1))
