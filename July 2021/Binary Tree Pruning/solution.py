# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def util(root):
            if root is None:
                return 0
            left = util(root.left)
            right = util(root.right)
            if left == 0:
                root.left = None
            if right == 0:
                root.right = None
            return max(left,right, root.val)
        
        util(root)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root
        