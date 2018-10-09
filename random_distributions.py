import random
import math


def uniform(high):
    return random.uniform(0, high)

def skewed(high):
    x = 1.0 - random.random()
    return high + (-1 * high) * math.sqrt(x)

def two_tiered(high, cutoff=0.1, first_portion=0.5):
    x = random.random()
    if x < first_portion:
        return random.uniform(0, high * cutoff)
    else:
        return random.uniform(high * cutoff, high)

def triangular(high, mode=None, low=0):
    x = random.random()
    mode = 0.5 if mode is None else (mode - low) / (high - low)
    if x > mode:
        x = 1.0 - x
        mode = 1.0 - mode
        low, high = high, low
    return low + (high - low) * math.sqrt(x * mode)

"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
N = 100
trials = 20000

y_pos = list(range(1,N+1))

py_performance = [0] * N
for i in range(trials):
    result = triangular(N)
    py_performance[int(result)] += 1
plt.bar(y_pos, py_performance, align="center", alpha=0.5)
plt.title('Triangular')
plt.show()
"""