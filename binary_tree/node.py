class Node():
    
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
       
    def set_value(self, value):
        self.value = value
        
    def get_value(self):
        return self.value
    
    def set_left_child(self, left):
        self.left = left
    
    def get_left_child(self):
        return self.left
    
    def set_right_child(self, right):
        self.right = right
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

if __name__ == '__main__':
    node = Node()
    node.set_value(20)
    node2 = Node(14)

    print(node)
    print(node2)
