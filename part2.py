
class DLLNode: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next
        self.prev = prev
        self.data = data

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return self.__str__()


class DLList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_front(self, new_data):
        """ push new node to front of DLL """
        new_node = DLLNode(data = new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def foreach(self, func, args):
        curr = self.head
        while curr:
            func(curr, args)
            curr = curr.next

    def del_node(self, session_id):
        if self.head is None:
            return
        curr = self.head
        while curr:
            if curr.data.session_id == session_id:
                if curr.prev:
                    if curr.next:
                        curr.next.prev = curr.prev
                        curr.prev.next = curr.next
                    else:
                        curr.prev.next = None
                else:
                    self.del_front()
            else:
                curr = curr.next
    
    def del_front(self):
        if self.head is not None:
            next_node = self.head.next
            self.head = None
            if next_node is not None:
                next_node.prev = None
                self.head = next_node
    
    def print_list(self):
        curr = self.head
        _str = "<<- "
        while curr:
            _str += str(curr) + " "
            curr = curr.next
        _str = _str[:-1]
        _str += " ->>"
        return _str
    
    def __str__(self):
        return self.print_list()
    
    def __repr__(self):
        return self.__str__()
                

class VertexData():
    def __init__(self, session_id, edges_ptr, curr_degree, color="red"):
        self.session_id = session_id
        self.edges_ptr = edges_ptr
        self.curr_degree = curr_degree
        self.color = color
    
    def __str__(self):
        return str(self.session_id)
    
    def __repr__(self):
        self.__str__()




def build_degree_array(P, E, N):
    """ method to create a map of degree -> DLList of vertices of this degree """

    def dllist_append(dllist, degree, vertex):
        """ internal function to build DLList dynamically """
        #print(degree)
        if dllist[degree] == False:
            dllist[degree] = DLList()
        dllist[degree].add_front(vertex)
    
    print("E:", E)
    print("P:", P)

    deg_dll_array = [False for x in range(N-1)]
    deg_ptr_array = [False for x in range(N)]

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
        vertex = VertexData(session_id, P[i], degree)
        dllist_append(deg_dll_array, degree, vertex)
        deg_ptr_array[i] = degree

    
    return deg_dll_array, deg_ptr_array


def smallest_last_ordering(N, S, K, DIST, P, E, M):
    deg_dll_array, deg_ptr_array = build_degree_array(P, E, N)
    print(deg_dll_array)
    print(deg_ptr_array)

    # delete vertices smallest vertex first recursively
    deleted_list = []

    # i = 0
    # while i < N-1:
    #     deg_plist[i].foreach(recur_delete, )




def part2_wrapper(N, S, K, DIST, P, E, M):
    """ wrapper method for part2 """
    smallest_last_ordering(N, S, K, DIST, P, E, M)
