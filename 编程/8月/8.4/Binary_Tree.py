__author__ = "Narwhale"

class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Tree(object):
    """二叉树"""
    def __init__(self,node=None):
        self.root = node

    def add(self,item):
        """添加"""
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def travel(self):
        """广度遍历"""
        if self.root == None:
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                print(cur.elem,end=' ')
                if cur.lchild:
                    queue.append(cur.lchild)
                if cur.rchild:
                    queue.append(cur.rchild)

    def preorder(self,node):
        """先序遍历"""
        #根 --> 左 --> 右
        if node is None:
            return

        print(node.elem,end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node):
        """中序遍历"""
        #左 --> 根 --> 右
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem,end=' ')
        self.inorder(node.rchild)


    def postorder(self,node):
        """后序遍历"""
        #左 --> 右 --> 根
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem,end=' ')




tree = Tree()
tree.add(0)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
tree.add(9)
tree.travel()
print(' ')
tree.preorder(tree.root)
print(' ')
tree.inorder(tree.root)
print(' ')
tree.postorder(tree.root)