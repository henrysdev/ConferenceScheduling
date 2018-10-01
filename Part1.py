"""
INPUT:
•	N = Number of sessions (MAX = 10,000)
•	S = Number of attendees. (MAX = 100,000)
•	K = Number of sessions per attendee. (MAX = N for uniform and two-tiered distributions;  MAX = 0.1N for Skewed distribution and your distribution)
•	DIST = UNIFORM | TIERED | SKEWED | YOURS
OUTPUT:
•	N = Number of sessions (may be reduced to actual number to be scheduled)
•	M = number of distinct pair-wise session conflicts.
•	T = Total number of pair-wise session conflicts.
•	S = Number of attendees.
•	K = Number of sessions per attendee.
•	DIST = UNIFORM | TIERED | SKEWED | YOURS
•	E[] = adjacency list of distinct session conflicts (length = 2M)
•	P[] = Pointer for each session I, 1 <= I <= N denoting the starting point in E[] of the list of sessions in conflict with session I. That is, the conflicts for session I are indicated in locations E[P[I]], E[P[I]+1], …, E[P[I+1]-1]. 
•	An example output file will be provided on Canvas.
"""
import random
import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def uniform(high):
    return random.uniform(0, high)

def skewed(high):
    x = 1.0 - random.random()
    return high + (-1 * high) * math.sqrt(x)

def two_tiered(high, cutoff=0.1, first_portion=0.5):
    x = random.random()
    if x < first_portion:
        return random.uniform(0, math.floor(N * cutoff))
    else:
        return random.uniform(math.floor(N * cutoff), N)

def triangular(high, mode):
    x = random.random()
    low = 0
    mode = 0.5 if mode is None else (mode - low) / (high - low)
    if x > mode:
        x = 1.0 - x
        mode = 1.0 - mode
        low, high = high, low
    return low + (high - low) * math.sqrt(x * mode)


def schedule_confs(N, S, K):
    # Uniform
    attendees = [0] * S
    for a in range(S):
        attendee_sessions = [0] * K
        for s in range(K):
            session = int(random.uniform(1, N))
            attendee_sessions[s] = session
        attendees[a] = attendee_sessions

    return attendees


N = 10
trials = 2000

y_pos = list(range(1,N+1))

py_performance = [0] * N
for i in range(trials):
    result = two_tiered(N) # uniform(N) # triangular(N,N//2)
    py_performance[int(result)] += 1
plt.bar(y_pos, py_performance, align="center", alpha=0.5)

plt.show()