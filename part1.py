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
import sys
import random_distributions

# keyword -> function map for rand distros
distributions = {
    'UNIFORM' : random_distributions.uniform,
    'TIERED'  : random_distributions.two_tiered,
    'SKEWED'  : random_distributions.skewed,
    'YOURS'   : random_distributions.triangular
}

def prettyprint(iterable):
    for item in iterable:
        print(sorted(list(item)))

def gen_attendee_sessions(N, S, K, DIST):
    dist_func = distributions[DIST]
    # allocate array of size (num_attendees * num_sessions_per_attendee)
    sessions = [0] * (S * K)
    for attendee in range(S):
        # loops until set is of size k (k distinct sessions)
        # TODO break out of loop condition for edge cases
        distinct_sessions = set()
        while len(distinct_sessions) < K:
            # get random session and add to set
            sess = int(dist_func(N))
            distinct_sessions.add(sess)
        # start position in sessions array to overwrite
        start = attendee * K
        # fill in segment of sessions array with new attendee sessions
        new_sessions = list(distinct_sessions)
        for i in range(0, K):
            sessions[i+start] = new_sessions[i]
    return sessions

def gen_conflicts(attendee_sessions, K):
    conflicts = set()
    j = 0
    while j < K:
        # get and remove last element of array
        a = attendee_sessions[j]
        for b in attendee_sessions:
            if b != a:
                conflicts.add((min(a,b), max(a,b)))
        j += 1
    return conflicts

def sessions_to_conflicts(sessions, S, K):
    conflicts = [[]] * S
    temp = [0] * K
    c, t = 0, 0
    for i in range(len(sessions)):
        if i % K == 0 and i > 0:
            conflicts[c] = gen_conflicts(temp, K)
            c += 1
            t = 0
        temp[t] = sessions[i]
        t += 1
    conflicts[c] = gen_conflicts(temp, K)
    return conflicts

def schedule_confs(N, S, K, DIST):
    # get 1D array of K unique sessions for S attendees
    sessions = gen_attendee_sessions(N, S, K, DIST)
    conflicts = sessions_to_conflicts(sessions, S, K)
    prettyprint(conflicts)


if __name__ == "__main__":
    # default algorithm arguments
    N = 120
    S = 32
    K = 12
    DIST = 'UNIFORM'
    
    # parse in commandline arguments
    if len(sys.argv) == 5:
        N = int(sys.argv[1])
        S = int(sys.argv[2])
        K = int(sys.argv[3])
        DIST = sys.argv[4]

    # assert DIST is a valid keyword
    if DIST not in distributions:
        print("not a valid value for DIST")
        exit(0)

    if K > N:
        print("K cannot be greater than N")
        exit(0)

    schedule_confs(N, S, K, DIST)