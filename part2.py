from dllist import DLList, DLLNode
import part2_algorithms
import utils


def build_degree_array(P, E, N):
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
        degree_ptrs[i] = degree

    return degree_ptrs

def color_sessions(deleted_stack, P, E, N):
    print("E", E)
    print("P", P)
    print("deleted_stack", deleted_stack)
    colored_verts = [False] * N
    color_ordered = []
    while deleted_stack:
        vert = deleted_stack.pop()
        session_id = vert.session_id - 1
        neighbors = E[P[session_id] : P[session_id] + vert.orig_degree]
        bad_colors = set([colored_verts[x-1].color for x in neighbors if colored_verts[x-1]])
        color = 1
        for i in range(1, len(neighbors) + 1):
            if i not in bad_colors:
                color = i
                break
        vert.color = color
        colored_verts[session_id] = vert
        color_ordered.append(vert)

    return color_ordered


def print_output(func, N, S, K, DIST, M, colored_verts, total_num_colors, avg_orig_degree, max_deg_deleted):
    print(func.__name__)
    print("N", N)
    print("S", S)
    print("K", K)
    print("DIST", DIST)
    print("M", M)
    print("colored_verts", colored_verts)
    print("total_num_colors", total_num_colors)
    print("avg_orig_degree", avg_orig_degree)
    print("max_deg_deleted", max_deg_deleted)


def algo_wrapper(func, N, S, K, DIST, P, E, M):
    """ wrapper method for part2 """
    degree_ptrs = build_degree_array(P, E, N)
    N, S, K, DIST, M, deleted_stack = func(degree_ptrs[:], N, S, K, DIST, P, E, M)
    colored_verts = color_sessions(deleted_stack, P, E, N)
    total_num_colors = len(set([v.color for v in colored_verts]))
    avg_orig_degree = sum([v.orig_degree for v in colored_verts]) / len(colored_verts)
    max_deg_deleted = max([v.curr_degree for v in colored_verts])

    #print_output(func, N, S, K, DIST, M, deleted_stack, total_num_colors, avg_orig_degree, max_deg_deleted)


def input(func, N, S, K, DIST, P, E, M):
    algo_wrapper(func, N, S, K, DIST, P, E, M)