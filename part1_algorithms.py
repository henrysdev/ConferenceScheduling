""" Algorithm implementations for part 1 of project """

def method1(conflicts, N):
    """
    O(N^2) Space Complexity

    Deduplicates 1-D array of conflicts + generated E and P
    arrays using an adjacency matrix.
    """
    # cast to a set to dedup conflicts
    unique_cons = set(conflicts)
    # record output variable M (# unique session conflicts)
    M = len(unique_cons)

    # O(n^2) space (N x N matrix)
    # allocate NxN adjacency matrix
    adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
    # fill in conflict intersections in 2-D grid of edges
    for y in range(N):
        for x in range(N):
            # adjust for 1-indexed representation
            conflict = (y+1,x+1)
            if conflict in unique_cons:
                adj_matrix[y][x] = 1
                adj_matrix[x][y] = 1

    # initialize E and P arrays
    E = [0] * M * 2
    P = [-1] * N
    tmp_ptr = 0
    # iterate through 2-D grid and fill in E and P arrays
    for y in range(N):
        edge_count = 0
        for x in range(N):
            # fill in E array when conflict found + adjust for 1-indexing
            if adj_matrix[y][x]:
                E[tmp_ptr + edge_count] = x + 1
                edge_count += 1
        # fill in P array with current ptr if if has any conflicts 
        if edge_count:
            P[y] = tmp_ptr
        tmp_ptr += edge_count

    return P, E, M

def method2(conflicts, N):
    """
    O(M) Space Complexity

    Deduplicates 1-D array of conflicts + generated E and P
    arrays using adjacency lists.
    """
    # cast to a set and back into list to dedup keys
    unique_cons = set(conflicts)
    # record output variable M (# unique session conflicts)
    M = len(unique_cons)
    
    # construct empty 2-D container for N empty arraylists
    adjacency_lists = [[] for _ in range(N)]
    # iterate through unique conflicts and build adjacency lists
    for (v1, v2) in unique_cons:
        adjacency_lists[v1-1].append(v2)
        adjacency_lists[v2-1].append(v1)

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

    return P, E, M