'''
SET 2
🌲 Binary Tree Level Order Traversal
✅ Problem Statement:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

📥 Input:
root: a reference to the root node of a binary tree.

Each TreeNode has:

python
Copy
Edit
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
📤 Output:
A list of lists, where each inner list represents a level of the tree, containing the node values at that level.

🔒 Constraints:
The number of nodes in the tree is in the range [0, 2000].

-1000 <= Node.val <= 1000.
'''

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

    def binary_tree_lot(self, bt):
        if bt is None:
            return []

        q = Que()
        q.enq(bt)

        arr_m = []

        while len(q.Q) > 0:
            size = len(q.Q)         # number of nodes at this level
            arr_n = []

            for _ in range(size):   # process one level at a time
                p = q.dq()
                arr_n.append(p.data)

                if p.lc is not None:
                    q.enq(p.lc)

                if p.rc is not None:
                    q.enq(p.rc)

            arr_m.append(arr_n)

        return arr_m

'''
MY ATTEMPT:

    def binary_tree_lot(self, bt):

        if bt.lc is None and bt.rc is None:
            return [bt.data]

        q = Que()
        q.enq(bt)

        arr_m = []

        while len(q.Q) > 0:
            arr_n = []
            p = q.dq()

            arr_n.append(p.data)

            if p.lc is not None:
                q.enq(p.lc)
                arr_n.append(p.lc.data)

            if p.rc is not None:
                q.enq(p.rc)
                arr_n.append(p.rc.data)

            arr_m.append(arr_n)

        return arr_m
'''

tree = Tree()

t = 0
arr = [1, 2, 3, 4, 5, None, 6]

for i in range(0, len(arr)):
    t = tree.add_to_tree(arr[i])

print(tree.binary_tree_lot(t))

'''
Main Take Aways: 

- 
'''