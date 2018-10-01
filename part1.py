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

def gen_attendee_sessions(N, S, K, dist_func):
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
        for i in range(K):
            sessions[i+start] = new_sessions[i]
    return sessions

def gen_conflicts(attendee_sessions, conflicts, K):
    attendee_conflicts = set()
    attendee_choices = []
    for i in range(K):
        # get and remove last element of array
        a = attendee_sessions[i]
        attendee_choices.append(a)
        for b in attendee_sessions:
            if b != a:
                conflict = tuple([min(a,b), max(a,b)])
                if conflict not in attendee_conflicts:
                    attendee_conflicts.add(tuple([min(a,b), max(a,b)]))
                    conflicts.append(conflict)
    print(attendee_choices)
    print(attendee_conflicts)

def sessions_to_conflicts(sessions, S, K):
    conflicts = []
    temp = [0] * K
    c, t = 0, 0
    for i in range(len(sessions)):
        if i % K == 0 and i > 0:
            gen_conflicts(temp, conflicts, K)
            c += 1
            t = 0
        temp[t] = sessions[i]
        t += 1
    gen_conflicts(temp, conflicts, K)
    return conflicts

def slow_dedup(conflicts, N):
    # cast to a set and back into list to dedup keys
    unique_cons = list(set(conflicts))
    # record output variable M (# unique session conflicts)
    M = len(conflicts)
    # iterate through unique conflicts and create adjacency matrix
    vertex_map = {}
    for i, (a,b) in enumerate(unique_cons):
        # edge a-->b
        if a in vertex_map:
            vertex_map[a].append(b)
        else:
            vertex_map[a] = [b]
        # edge b-->a
        if b in vertex_map:
            vertex_map[b].append(a)
        else:
            vertex_map[b] = [a]
    # build pointer list for each meeting
    # set pointer to -1 by default if meeting
    # has no conflicts
    P = [-1] * N
    keys = set(vertex_map.keys())
    ptr = 0
    for i in range(1,N+1):
        if i in keys:
            P[i-1] = ptr
            ptr += len(vertex_map[i])
    # flatten matrix into adjacency list
    E = []
    values = vertex_map.values()
    for sublist in values:
        for item in sublist:
            E.append(item)

    print("P:",P)
    print("E:",E)
    print("M:",M)

    return None


def schedule_confs(N, S, K, DIST):
    # get 1D array of K unique sessions for S attendees
    sessions = gen_attendee_sessions(N, S, K, distributions[DIST])
    conflicts = sessions_to_conflicts(sessions, S, K)
    # V1 and V2
    unique_conflicts = slow_dedup(conflicts, N)


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