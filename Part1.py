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

def schedule_confs(N, S, K):
    # allocate array of size (num_attendees * num_sessions_per_attendee)
    sessions = [0] * (S * K)
    for attendee in range(S):
        # loops until set is of size k (k distinct sessions)
        # TODO break out of loop condition for edge cases
        distinct_sessions = set()
        while len(distinct_sessions) < K:
            distinct_sessions.add(int(random.uniform(1, N)))
        # start position in sessions array to overwrite
        start = attendee * K
        # cast set of distinct sessions to a list for storage in sessions array
        new_sessions = list(distinct_sessions)
        print(new_sessions)
        for i in range(0, K):
            sessions[i+start] = new_sessions[i]
    return sessions

schedule_confs(N=120,S=32,K=12)

"""
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