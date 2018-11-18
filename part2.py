
class DLLNode: 
    
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next
        self.prev = prev
        self.data = data

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)

class DLList:

    def __init__(self):
        self.head = None

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
        _str = ""
        while curr:
            _str += str(curr) + " "
            curr = curr.next
        return _str
    
    def __str__(self):
        return self.print_list()
    
    def __repr__(self):
        return self.print_list()
                

class VertexData():
    def __init__(self, session_id, degree, color="red"):
        self.session_id = session_id
        self.degree = degree
        self.color = color
    
    def __str__(self):
        return """
sess_id: {}, degree: {}, color: {}
        """.format(self.session_id, self.degree, self.color)
    
    def __repr__(self):
        return """sess_id: {}, degree: {}, color: {}""".format(self.session_id, self.degree, self.color)

def _dict_dllist_append(_dict, degree, vertex):
    if degree not in _dict:
        _dict[degree] = DLList()
    _dict[degree].add_front(vertex)


def build_degree_map(P, E):
    deg_to_plist = {}

    j = 0
    k = 0

    while j < len(P):
        if P[j] == -1:
            degree = 0
            session_id = j + 1
            vertex = VertexData(session_id, degree)
            _dict_dllist_append(deg_to_plist, degree, vertex)
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
            vertex = VertexData(session_id, degree)
            _dict_dllist_append(deg_to_plist, degree, vertex)

            if next_val != len(E):
                j = k
            else:
                break
    
    return deg_to_plist


def smallest_last_ordering(N, S, K, DIST, P, E, M):
    deg_to_plist = build_degree_map(P, E)
    print(deg_to_plist)
    # for key in deg_to_plist:
    #     print(deg_to_plist[key])