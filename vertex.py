class VertexData():
    def __init__(self, session_id, edges_ptr, curr_degree, orig_degree, color="red"):
        self.session_id = session_id
        self.edges_ptr = edges_ptr
        self.curr_degree = curr_degree
        self.orig_degree = orig_degree
        self.color = color
    
    def __str__(self):
        return "\n<< color: {}, session_id: {}, orig_deg: {}, deg_deleted: {} >>\n".format(self.color, self.session_id, self.orig_degree, self.curr_degree)
    
    def __repr__(self):
        return self.__str__()