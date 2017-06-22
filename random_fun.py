import numpy as np

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')


def bs_replicate(data, func=np.mean):
    """Compute a bootstrap replicate from data."""
    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)

def draw_bs_reps(data, func=np.mean, size=10000):
    """Draw bootstrap replicates from 1D data."""
    return np.array([bs_replicate(data, func=func) for _ in range(size)])

# Generate lots of replicates.
n_reps = 100000

bs_reps = [bs_replicate(bd_2012, func=np.mean) for _ in range(n_reps)]
