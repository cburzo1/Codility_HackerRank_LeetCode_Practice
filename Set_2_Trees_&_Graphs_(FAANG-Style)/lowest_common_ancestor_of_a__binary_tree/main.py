class Node:
    def __init__(self, val):
        self.data = val
        self.lc = None
        self.rc = None

class Que:
    def __init__(self):
        self.Q = []

    def enq(self, val):
        self.Q.append(val)

    def dq(self):
        if len(self.Q) > 0:
            return self.Q.pop(0)
        else:
            return "is empty"

class Tree:
    def __init__(self):
        self.root = None
        self.list_t = []

    def add_to_tree(self, val):
        node = Node(val)

        if self.root is None:
            self.root = node
            return self.root

        que = Que()
        que.enq(self.root)

        while len(que.Q) > 0:
            p = que.dq()
            if p.lc is not None:
                que.enq(p.lc)
            else:
                p.lc = node
                break

            if p.rc is not None:
                que.enq(p.rc)
            else:
                p.rc = node
                break

        return self.root

    def preorder(self, p, val):
        if p.data == val and p.data is not None:
            return

        if p.data is not None:
            print(p.data, end=" ")
            self.list_t.append(p.data)

        self.preorder(p.lc, val)
        self.preorder(p.rc, val)

    def lowest_common_ancestor(self, t, p, q):
        self.preorder(t, p)
        print(self.list_t)

tree = Tree()

#tree.add_to_tree(5)
#tree.add_to_tree(2)

t = 0
arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

for i in range(0, len(arr)):
    t = tree.add_to_tree(arr[i])


#tree.inorder(t)

tree.lowest_common_ancestor(t, 6, 4)