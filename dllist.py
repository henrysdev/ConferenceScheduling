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
    
    def append(self, new_data):
        new_node = Node(data = new_data) 
        last = self.head 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return
        while (last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 

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