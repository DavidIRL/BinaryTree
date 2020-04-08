from node import Node
from queue import Queue

class Tree():

    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def search(self, value):
        s_value = Node(value)
        node = self.get_root()
        while(True):
            comparison = self.compare(node, s_value)
            if comparison == 0:
                # value was found in Tree so return True and break
                return True
            elif comparison == -1:
                if node.has_left_child():
                    # Node is greater than value and has left child, use to compare to value
                    node = node.get_left_child()
                else:
                    # traversed all less than Nodes, but value wasn't found so return False and break
                    return False
            else:
                if node.has_right_child():
                    # Node is less than value and has right child, use to compare to value
                    node = node.get_right_child()
                else:
                    # traversed all less than Nodes, but value wasn't found so return False and break
                    return False
    
    def compare(self, node, new_node):
        # when tree contains values that can be mathematiclly compared
        if new_node.get_value() == node.get_value():
            return 0 # current node and new_node are equals
        elif new_node.get_value() < node.get_value():
            return -1 # current node is greater than new_node
        else: 
            return 1 # current node is less than new_node
        
    def insert(self, value):
        if self.get_root() == None:
            self.set_root(value)
            return
        # Tree has root, begin searching for Node placement
        self.recurse_insert(self.get_root(), Node(value))
        
    def recurse_insert(self, node, new_node):
        if node.get_value() == None:
            node.set_value(new_node.get_value())
        
        comparison = self.compare(node, new_node)
        if comparison == 0:
            node.set_value(new_node.get_value())
            # we'll be overwriting duplicates
        elif comparison == -1:
            if node.has_left_child():
                # current node has left child so compare it to new_node
                self.recurse_insert(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)
        else:
            if node.has_right_child():
                #current node has right child so compare it to new_node
                self.recurse_insert(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)

    def __repr__(self):
        q = Queue()
        visit_order = []
        node = self.get_root()
        q.enq( (node) )
        while(len(q) > 0):
            node = q.deq()
            if node == None:
                visit_order.append('<empty>')
                continue
            else:
                visit_order.append(node)
            if node.has_left_child():
                q.enq(node.get_left_child())
            else:
                q.enq('<empty')

            if node.has_right_child():
                q.enq(node.get_right_child())
            else:
                q.enq('<empty>')

        viz = "Tree\n"
        previous_level = -1
        # loop through tree printing values while keeping track of
        # level and level -1 to know when to print to new line
        for i in range(len(visit_order)):
            node = visit_order[i]
            viz += " | " + str(node) 
       
        return viz


if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(15)
    tree.insert(20)
    tree.insert(70)
    tree.insert(5)
    tree.insert(30)
    tree.insert(10) # insert duplicate
    tree.insert(36)
    tree.insert(1)
    tree.insert(40)
    tree.insert(32)

    print('Is 20 in tree? ' + str(tree.search(20)))
    print('Is 45 in tree? ' + str(tree.search(45)))
    print('Is 1 in tree? ' + str(tree.search(1)))
    print('Is 36 in tree? ' + str(tree.search(36)))