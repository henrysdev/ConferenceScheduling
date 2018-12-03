from dllist import DLList, DLLNode
import part2_algorithms
import utils


def build_degree_array(P, E, N):
    """ method to create a map of degree -> DLList of vertices of this degree """
    
    print("E:", E)
    print("P:", P)

    degree_ptrs = [False for x in range(N)]

    saved_val = len(E)
    for i in range(len(P)-1, -1 , -1):
        if P[i] == -1:
            degree = 0
        elif saved_val:
            degree = saved_val - P[i]
            saved_val = P[i]
        else:
            saved_val = P[i]
            continue
        session_id = i + 1
        degree_ptrs[i] = degree

    return degree_ptrs

def print_output(N, S, K, DIST, M, deleted_stack, total_num_colors, avg_orig_degree, max_deg_deleted):
    print(func.__name__)
    print("N", N)
    print("S", S)
    print("K", K)
    print("DIST", DIST)
    print("M", M)
    print("deleted_stack", deleted_stack)
    print("total_num_colors", total_num_colors)
    print("avg_orig_degree", avg_orig_degree)
    print("max_deg_deleted", max_deg_deleted)

"""
N = Number of sessions (may be reduced to actual number to be scheduled)
M = number of distinct pair-wise session conflicts.
T = Total number of pair-wise session conflicts.
S = Number of attendees.
K = Number of sessions per attendee.
"""


def algo_wrapper(func, N, S, K, DIST, P, E, M):
    """ wrapper method for part2 """
    degree_ptrs = build_degree_array(P, E, N)
    N, S, K, DIST, M, deleted_stack = func(degree_ptrs[:], N, S, K, DIST, P, E, M)
    total_num_colors = len(set([v.color for v in deleted_stack]))
    avg_orig_degree = sum([v.orig_degree for v in deleted_stack]) / len(deleted_stack)
    max_deg_deleted = max([v.curr_degree for v in deleted_stack])

    N, S, K, DIST, M, deleted_stack, total_num_colors, avg_orig_degree, max_deg_deleted


def plot_func(func, N, S, K, DIST, P, E, M):
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import matplotlib.pyplot as plt

    asymp_range = range(10,1000)
    y_axis = [0 for x in len(asymp_range)]
    x_axis = list(asymp_range)

    for val in asymp_range:
        start = time.time()
        algo_wrapper(func, N=val, S=S, K=K, DIST=DIST, P=P, E=E, M=M)
        end = time.time()
        y_axis[val] = end - start
    
    plt.plot(y_axis, x_axis)
    plt.show()

def input(N, S, K, DIST, P, E, M):
    funcs = [
        part2_algorithms.smallest_last_ordering,
        part2_algorithms.random_ordering
    ]
    for f in funcs:
        #algo_wrapper(f, N, S, K, DIST, P, E, M)
        plot_func(f, N, S, K, DIST, P, E, M)