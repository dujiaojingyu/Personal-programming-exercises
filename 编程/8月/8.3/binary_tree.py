__author__ = "Narwhale"

class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self,node=None):
        self.root = node

    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
        queue = []
        queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)


tree = Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
