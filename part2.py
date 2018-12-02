from dllist import DLList, DLLNode
import part2_algorithms


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


def part2_wrapper(N, S, K, DIST, P, E, M):
    """ wrapper method for part2 """
    degree_ptrs = build_degree_array(P, E, N)
    print("SMALLEST_LAST_ORDERING")
    N, S, K, DIST, M, deleted_stack = part2_algorithms.smallest_last_ordering(degree_ptrs[:], N, S, K, DIST, P, E, M)
    print("N", N)
    print("S", S)
    print("K", K)
    print("DIST", DIST)
    print("M", M)
    print("deleted_stack", deleted_stack)

    # print("RANDOM ORDERING")
    # part2_algorithms.random_ordering(degree_ptrs[:], N, S, K, DIST, P, E, M)