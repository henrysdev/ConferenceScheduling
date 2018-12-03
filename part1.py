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
import random_distributions as rand_distros
import part1_algorithms as p1_algos
import part2
import part2_algorithms
import utils
import time


# keyword -> function map for rand distros
distributions = {
    'UNIFORM' : rand_distros.uniform,
    'TIERED'  : rand_distros.two_tiered,
    'SKEWED'  : rand_distros.skewed,
    'YOURS'   : rand_distros.triangular
}

def pick_attendee_sessions(N, S, K, dist_func=rand_distros.uniform):
    """
    pick K attendee sessions for each of N attendees using the
    provided random distribution functions and them as a 1-D array
    """
    # allocate array of size (num_attendees * num_sessions_per_attendee)
    sessions = [0] * (S * K)
    for attendee in range(S):
        # loops until set is of size k (k distinct sessions)
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

def gen_conflicts(att_sessions, conflicts, ptr, K):
    """
    generate (K*(K-1))/2 conflict pairs for a given attendee's
    session array
    """
    attendee_conflicts = set()
    tmp_idx = ptr
    # iterate through attendee's sessions and build conflict pairs (edges)
    for sess1 in att_sessions:
        # iterate through 
        for sess2 in att_sessions:
            # prevent generating session conflict with itself
            if sess1 != sess2:
                # note that this sort will ALWAYS only sort 2 items,
                # therefore it is not O(nlogn), but O(2) -> O(1) (constant time)
                first, second = min(sess1, sess2), max(sess1, sess2)
                conflict = (first, second)
                # add new conflict to seen set if unique.
                # append by reference to master conflicts set
                if conflict not in attendee_conflicts:
                    conflicts[tmp_idx] = conflict
                    attendee_conflicts.add(conflict)
                    tmp_idx += 1

def sessions_to_conflicts(sessions, S, K):
    """
    transform 1-D array of attendees (each with K sessions)
    into a 1-D array of conflict pairs (session1, session2)
    """
    # allocate master conflict array of session pairs (edges)
    conflicts = [(-1,-1)] * (S * ((K*(K-1))//2))
    temp_buf = [0] * K
    # t being index in temp buffer, ptr being index in conflict array
    # that we are filling 
    t, ptr = 0, 0
    for i in range(K * S):
        # every Kth increment, temp buf represents one attendee,
        # therefore, generate conflicts for the current attendee
        if not i % K and i > 0:
            gen_conflicts(temp_buf, conflicts, ptr, K)
            ptr += (K * (K-1)) // 2
            t = 0
        temp_buf[t] = sessions[i]
        t += 1
    # generate conflicts for the last attendee
    gen_conflicts(temp_buf, conflicts, ptr, K)
    return conflicts

def schedule_confs(func, N, S, K, DIST):
    """
    primary algorithm harnessing method
    """
    global distributions
    # get 1D array of K unique sessions for S attendees
    sessions = pick_attendee_sessions(N, S, K, distributions[DIST])
    # generate conflicts for these sessions
    conflicts = sessions_to_conflicts(sessions, S, K)

    for method in [p1_algos.method1, p1_algos.method2]:
        P, E, M = method(conflicts, N)
        return part2.input(func, N=N, S=S, K=K, DIST=DIST, P=P, E=E, M=M)
        #return utils.format_output(N=N, S=S, K=K, DIST=DIST, P=P, E=E, M=M)




def plot_func(funcs, N, S, K, DIST, trials=3):
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import matplotlib.pyplot as plt

    indep_var = "S"

    for func in funcs:
        asymp_range = range(12, 2000)
        y_axis = []
        x_axis = list(asymp_range)

        for val in asymp_range:
            trials_time = 0.0
            for _ in range(trials):
                start = time.time()
                schedule_confs(func=func, N=N, S=val, K=K, DIST=DIST)
                end = time.time()
                trials_time += (end - start)
            y_axis.append(trials_time / trials)
        plt.plot(x_axis, y_axis)

    plt.ylabel('Time')
    plt.xlabel(indep_var)
    plt.title('CPU Time vs {}'.format(indep_var))
    plt.legend(tuple([f.__name__ for f in funcs]), loc='best' )
    plt.savefig("part2_screenshots/time_vs_{}.png".format(indep_var))
    plt.show()

def plot_wrapper(N, S, K, DIST):
    funcs = [
        part2_algorithms.smallest_last_ordering,
        part2_algorithms.random_ordering
    ]
    plot_func(funcs, N, S, K, DIST)



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
    
    # plot_wrapper(N, S, K, DIST)
    # exit(0)

    # **** Edge Cases ****
    # exit if DIST is a valid keyword
    if DIST not in distributions:
        print("not a valid value for DIST")
        exit(0)
    # exit if K is greater than N
    if K > N:
        print("K cannot be greater than N")
        exit(0)
    # exit if N is less than 2
    if not N or not S or not K:
        print("All parameters must be positive")
        exit(0)

    func = part2_algorithms.smallest_last_ordering
    output = schedule_confs(func, N, S, K, DIST)