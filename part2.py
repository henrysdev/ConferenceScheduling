
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
        print(self.edges_ptr)
        return str(self.edges_ptr)
    
    def __repr__(self):
        self.__str__()




def build_degree_map(P, E, N):
    """ method to create a map of degree -> DLList of vertices of this degree """

    def _dllist_append(_plist, degree, vertex):
        """ internal function to build DLList dynamically """
        if _plist[degree] == False:
            _plist[degree] = DLList()
        _plist[degree].add_front(vertex)

    deg_to_plist = [False for x in range(N-1)]

    j = 0
    k = 0

    while j < len(P):
        if P[j] == -1:
            degree = 0
            session_id = j + 1
            vertex = VertexData(session_id, P[j], degree)
            _dllist_append(deg_to_plist, degree, vertex)
            j += 1
        else:
            next_val = len(E)
            k = j + 1
            while k < len(P):
                if P[k] == -1:
                    k += 1
                else:
                    next_val = P[k]
                    break
            degree = next_val - P[j]
            session_id = j + 1
            vertex = VertexData(session_id, P[j], degree)
            _dllist_append(deg_to_plist, degree, vertex)

            if next_val != len(E):
                j = k
            else:
                break
    
    return deg_to_plist


def smallest_last_ordering(N, S, K, DIST, P, E, M):
    deg_to_plist = build_degree_map(P, E, N)
    print(deg_to_plist)
    # delete vertices smallest vertex first recursively
    deleted_list = []



def part2_wrapper(N, S, K, DIST, P, E, M):
    """ wrapper method for part2 """
    smallest_last_ordering(N, S, K, DIST, P, E, M)
