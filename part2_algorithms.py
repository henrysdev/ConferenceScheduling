import random
from vertex import VertexData


def smallest_last_ordering(degree_ptrs, N, S, K, DIST, P, E, M):

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
        degree_ptrs[session_id] = -1
    
    def update_vertex(session_id, degree_ptrs, N):
        if degree_ptrs[session_id] > 0:
            degree_ptrs[session_id] -= 1
    
    #print("degree ptrs", degree_ptrs)

    orig_degrees = degree_ptrs[:]
    
    deleted_stack = []

    # delete vertices smallest vertex first recursively
    # find first smallest vertex as starting point
    while len(deleted_stack) < N:
        curr_session, curr_degree = find_next_smallest(degree_ptrs, N)
        neighbors = E[P[curr_session] : P[curr_session] + orig_degrees[curr_session]]
        # decrement the number of connections for each neighboring vertex by 1
        for n in neighbors:
            update_vertex(n - 1, degree_ptrs, N)
        
        saved_vert = VertexData(curr_session + 1, P[curr_session], curr_degree, orig_degrees[curr_session])
        delete_vertex(curr_session, degree_ptrs)
        deleted_stack.append(saved_vert)

    deleted_stack = deleted_stack[::-1]
    for i in range(len(deleted_stack)):
        deleted_stack[i].color = i + 1

    num_colors_used = len(deleted_stack)

    return N, S, K, DIST, M, deleted_stack

def random_ordering(degree_ptrs, N, S, K, DIST, P, E, M):

    def pick_next(degree_ptrs, verts_left):
        rand_idx = random.choice(verts_left)
        rand_deg = degree_ptrs[rand_idx]
        return rand_idx, rand_deg
    
    def delete_vertex(session_id, degree_ptrs):
        degree_ptrs[session_id] = -1
    
    def update_vertex(session_id, degree_ptrs, N):
        if degree_ptrs[session_id] > 0:
            degree_ptrs[session_id] -= 1
    
    #print("degree ptrs", degree_ptrs)
    
    verts_left = list(range(len(degree_ptrs)))
    orig_degrees = degree_ptrs[:]
    deleted_stack = []

    while len(deleted_stack) < N:
        curr_session, curr_degree = pick_next(degree_ptrs, verts_left)
        neighbors = E[P[curr_session] : P[curr_session] + orig_degrees[curr_session]]
        # decrement the number of connections for each neighboring vertex by 1
        for n in neighbors:
            update_vertex(n - 1, degree_ptrs, N)
        
        saved_vert = VertexData(curr_session + 1, P[curr_session], curr_degree, orig_degrees[curr_session])
        delete_vertex(curr_session, degree_ptrs)
        verts_left.remove(curr_session)
        deleted_stack.append(saved_vert)

    deleted_stack = deleted_stack[::-1]
    for i in range(len(deleted_stack)):
        deleted_stack[i].color = i + 1

    num_colors_used = len(deleted_stack)

    return N, S, K, DIST, M, deleted_stack