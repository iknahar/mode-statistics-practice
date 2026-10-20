import numpy as np
#
# a made-up week of 1,000 gym check-ins, in hours after midnight
def load_times(seed=21):
    rng = np.random.default_rng(seed)
    early = rng.normal(7.0, 0.55, 360)       # the before-work crowd
    late = rng.normal(18.4, 1.2, 570)        # the after-work crowd
    drop = rng.uniform(8.5, 16.5, 70)        # people with odd shifts
    return np.concatenate([early, late, drop])
#
def hhmm(hours):
    m = int(round(hours * 60))               # hours to whole minutes
    return f"{m // 60:02d}:{m % 60:02d}"
