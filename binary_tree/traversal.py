from tree import Tree

def pre_order(tree):
    visit_order = []
    root = tree.get_root()
  
    def traverse(node):
      if node:
        visit_order.append(node.get_value())
        traverse(node.get_left_child())
        traverse(node.get_right_child())
      
    traverse(root)
  
    return visit_order
  
 
def in_order(tree):
    visit_order = []
    root = tree.get_root()
  
    def traverse(node):
      if node:
        traverse(node.get_left_child())
        visit_order.append(node.get_value())
        traverse(node.get_right_child())
      
    traverse(root)
  
    return visit_order


def post_order(tree):
    visit_order = []
    root = tree.get_root()

    def traverse(node):
      if node:
        traverse(node.get_left_child())
        traverse(node.get_right_child())
        visit_order.append(node.get_value())

    traverse(root)

    return visit_order


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

    print(pre_order(tree))
    print(in_order(tree))
    print(post_order(tree))