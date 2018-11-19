from dllist import DLList, DLLNode

class VertexData():
    def __init__(self, session_id, edges_ptr, curr_degree, orig_degree, color="red"):
        self.session_id = session_id
        self.edges_ptr = edges_ptr
        self.curr_degree = curr_degree
        self.orig_degree = orig_degree
        self.color = color
    
    def __str__(self):
        return str(self.session_id)
    
    def __repr__(self):
        return self.__str__()




def build_degree_array(P, E, N):
    """ method to create a map of degree -> DLList of vertices of this degree """

    def dllist_append(dllist, degree, vertex):
        """ internal function to build DLList dynamically """
        if dllist[degree] == False:
            dllist[degree] = DLList()
        dllist[degree].add_front(vertex)
    
    print("E:", E)
    print("P:", P)

    degree_dllists = [False for x in range(N)]
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
        vertex = VertexData(session_id, P[i], P[i], degree)
        dllist_append(degree_dllists, degree, vertex)
        degree_ptrs[i] = degree

    return degree_dllists, degree_ptrs


def smallest_last_ordering(N, S, K, DIST, P, E, M):
    degree_dllists, degree_ptrs = build_degree_array(P, E, N)
    print(degree_dllists)
    print(degree_ptrs)

    orig_degrees = degree_ptrs[:]

    # delete vertices smallest vertex first recursively
    deleted_stack = []

    next_vert = None

    def find_next_smallest(degree_ptrs, N):
        min_degree = N
        min_idx = -1
        for i, elem in enumerate(degree_ptrs):
            if elem == 0:
                return i, elem
            if elem < min_degree and elem >= 0:
                min_degree = elem
                min_idx = i
        return min_idx, min_degree
    
    def delete_vertex(session_id, degree_ptrs):
        degree_ptrs[session_id] = -999
    
    def update_vertex(session_id, degree_ptrs, N):
        if degree_ptrs[session_id] > 0:
            degree_ptrs[session_id] -= 1

    # find first smallest vertex as starting point
    while len(deleted_stack) < N:
        curr_session, curr_degree = find_next_smallest(degree_ptrs, N)
        neighbors = E[P[curr_session] : P[curr_session] + orig_degrees[curr_session]]
        for n in neighbors:
            update_vertex(n - 1, degree_ptrs, N)
        
        saved_vert = VertexData(curr_session + 1, P[curr_session], curr_degree, orig_degrees[curr_session])
        delete_vertex(curr_session, degree_ptrs)
        deleted_stack.append(saved_vert)

    deleted_stack = deleted_stack[::-1]
    for i in range(len(deleted_stack)):
        deleted_stack[i].color = i + 1
    
    print(deleted_stack)
    

def part2_wrapper(N, S, K, DIST, P, E, M):
    """ wrapper method for part2 """
    smallest_last_ordering(N, S, K, DIST, P, E, M)