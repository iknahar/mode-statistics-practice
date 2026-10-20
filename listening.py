import numpy as np
#
# a made-up month of my music: 900 plays, in hours after midnight
# (24.5 means 00:30, the song you swore was your last one)
def load_plays(seed=21):
    rng = np.random.default_rng(seed)
    bus = rng.normal(8.0, 0.4, 340)          # the bus ride to uni
    bed = rng.normal(22.5, 0.75, 480)        # bedtime
    day = rng.uniform(10, 20, 80)            # random plays in between
    plays = np.concatenate([bus, bed, day])
    return plays[(plays >= 6) & (plays < 25)]
#
def hhmm(hours):
    m = int(round(hours * 60)) % (24 * 60)   # hours to whole minutes
    return f"{m // 60:02d}:{m % 60:02d}"
