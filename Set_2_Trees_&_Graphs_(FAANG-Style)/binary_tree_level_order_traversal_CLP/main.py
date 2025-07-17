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

