import random
import math

def uniform_distro(high):
    return random.uniform(0, high)

def skewed_distro(high):
    x = 1.0 - random.random()
    return high + (-1 * high) * math.sqrt(x)

def two_tiered_distro(high, cutoff=0.1, first_portion=0.5):
    x = random.random()
    if x < first_portion:
        return random.uniform(0, math.floor(N * cutoff))
    else:
        return random.uniform(math.floor(N * cutoff), N)

def triangular_distro(high, mode):
    x = random.random()
    mode = 0.5 if mode is None else (mode - low) / (high - low)
    if x > mode:
        x = 1.0 - x
        mode = 1.0 - mode
        low, high = high, low
    return low + (high - low) * math.sqrt(x * mode)

""" SAVE SAVE SAVE SAVE SAVE
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
N = 10
trials = 2000

y_pos = list(range(1,N+1))

py_performance = [0] * N
for i in range(trials):
    result = uniform_distro(N) #two_tiered(N) # uniform(N) # triangular(N,N//2)
    py_performance[int(result)] += 1
plt.bar(y_pos, py_performance, align="center", alpha=0.5)
plt.title('Uniform')
plt.show()
"""