'''
SET 2
🧩 Problem: Lowest Common Ancestor of a Binary Tree
Problem Statement
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q.

The lowest common ancestor is defined as:

“The lowest node in the tree that has both p and q as descendants.”
(A node can be a descendant of itself.)

📦 Constraints
The number of nodes in the tree is in the range [2, 10⁵]

-10⁹ <= Node.val <= 10⁹

All Node.val values are unique

Both p and q will exist in the tree

The tree is not necessarily a Binary Search Tree (important!)
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

    def lowest_common_ancestor(self, t, p, q):
        # Get path to p
        self.list_t = []
        self.preorder(t, p)
        path_p = list(self.list_t)  # Make a copy

        # Get path to q
        self.list_t = []
        self.preorder(t, q)
        path_q = list(self.list_t)  # Make a copy

        # Compare paths to find lowest common ancestor
        lca = None
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] == path_q[i]:
                lca = path_p[i]
            else:
                break

        return lca

    def preorder(self, p, val):
        if p is None:
            return False

        self.list_t.append(p.data)
        print(p.data, end=" ")

        if p.data == val:
            return True

        # Try left
        b = self.preorder(p.lc, val)
        if b is True:
            return True

        # Try right
        b = self.preorder(p.rc, val)
        if b is True:
            return True

        # If neither worked, backtrack
        self.list_t.pop()
        return False

tree = Tree()

t = 0
arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

for i in range(0, len(arr)):
    t = tree.add_to_tree(arr[i])

tree.lowest_common_ancestor(t, 6, 4)

'''
Main Take Aways: 
- Building a binary tree in python

- Creating an external Que for level-order tree creation

- Finding the path from root to a desired id

- in recursion, returning false when an id is not found and then when the root is found, bubble up while
returning true
'''