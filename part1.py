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


def schedule_confs(N, S, K, DIST):
    distributions = {
        'UNIFORM' : random_distributions.uniform,
        'TIERED'  : random_distributions.two_tiered,
        'SKEWED'  : random_distributions.skewed,
        'YOURS'   : random_distributions.triangular
    }
    if DIST not in distributions:
        print("not a valid value for DIST")
        exit(0)
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
        # cast set of distinct sessions to a list for storage in sessions array
        new_sessions = list(distinct_sessions)
        print(new_sessions)
        for i in range(0, K):
            sessions[i+start] = new_sessions[i]
    return sessions


if __name__ == "__main__":
    if len(sys.argv) == 5:
        N = int(sys.argv[1])
        S = int(sys.argv[2])
        K = int(sys.argv[3])
        DIST = sys.argv[4]
        schedule_confs(N, S, K, DIST)
    else:
        schedule_confs(N=120, S=32, K=12, DIST='UNIFORM')