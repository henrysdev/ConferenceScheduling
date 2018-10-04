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
import math
import random_distributions

# keyword -> function map for rand distros
distributions = {
    'UNIFORM' : random_distributions.uniform,
    'TIERED'  : random_distributions.two_tiered,
    'SKEWED'  : random_distributions.skewed,
    'YOURS'   : random_distributions.triangular
}

def prettyprint(iterable):
    for row in iterable:
        print(row)

def gen_attendee_sessions(N, S, K, dist_func):
    # allocate array of size (num_attendees * num_sessions_per_attendee)
    sessions = [0] * (S * K)
    for attendee in range(S):
        # loops until set is of size k (k distinct sessions)
        # TODO break out of loop condition for edge cases
        distinct_sessions = set()
        while len(distinct_sessions) < K:
            # get random session and add to set
            sess = math.ceil(dist_func(N))
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
                # note that this sort will ALWAYS only sort 2 items,
                # therefore it is not O(nlogn), but O(2) -> O(1) (constant time)
                conflict = tuple(sorted([a,b]))
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
        if not i % K and i > 0:
            gen_conflicts(temp, conflicts, K)
            c += 1
            t = 0
        temp[t] = sessions[i]
        t += 1
    gen_conflicts(temp, conflicts, K)
    return conflicts


# O(M) Space Complexity (Adjacency List Approach)
def method2(conflicts, N):
    # cast to a set and back into list to dedup keys
    unique_cons = list(set(conflicts))
    # record output variable M (# unique session conflicts)
    M = len(unique_cons)
    
    # construct container for N empty arraylists
    adjacency_lists = [[] for _ in range(N)]
    # iterate through unique conflicts and build adjacency lists
    for (v1, v2) in unique_cons:
        adjacency_lists[v1-1].append(v2)
        adjacency_lists[v2-1].append(v1)

    print(adjacency_lists)
    # initialize E and P arrays
    E = [0] * M * 2
    P = [-1] * N
    tmp_ptr = 0
    # fill in E and P arrays iteratively
    for i in range(N):
        listlen = len(adjacency_lists[i])
        for j in range(listlen):
            E[tmp_ptr + j] = adjacency_lists[i][j]
        if listlen:
            P[i] = tmp_ptr
        tmp_ptr += listlen

    print("P:",P)
    print("E:",E)
    print("M:",M)

    return None


# O(N^2) Space Complexity (Adjacency Matrix Approach)
def method1(conflicts, N):
    # cast to a set to dedup conflicts
    unique_cons = set(conflicts)
    # record output variable M (# unique session conflicts)
    M = len(unique_cons)

    # O(n^2) space (N x N matrix)
    adj_matrix = [[0] * N for _ in range(N)]#[[0] * N] * N
    for y in range(N):
        for x in range(N):
            # note that this sort will ALWAYS only sort 2 items,
            # therefore it is not O(nlogn), but O(2) -> O(1) (constant time)
            conflict = (y+1,x+1)
            if conflict in unique_cons:
                adj_matrix[y][x] = 1

    prettyprint(adj_matrix)
    # build P and E lists
    E = [0] * M * 2
    P = [-1] * N
    tmp_ptr = 0
    for y in range(N):
        edge_count = 0
        for x in range(N):
            if adj_matrix[y][x]:
                edge_count += 1
                E[tmp_ptr + x] = y
        if edge_count:
            P[y] = tmp_ptr
        tmp_ptr += edge_count

    print("P:",P)
    print("E:",E)
    print("M:",M)

    return None




def schedule_confs(N, S, K, DIST):
    # get 1D array of K unique sessions for S attendees
    sessions = gen_attendee_sessions(N, S, K, distributions[DIST])
    conflicts = sessions_to_conflicts(sessions, S, K)
    c1 = conflicts
    c2 = conflicts
    # V1 and V2
    unique_conflicts = method1(c1, N)
    #unique_conflicts = method2(c2, N)


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