# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorder(self,root:TreeNode):
#   traveling postorder traversal
        if root is None:
            return
        root.left and self.inoder(root.left)
        root.right and self.inoder(root.right)
#         switching the left and right subtree
        temp  = root.left
        root.left = root.right
        root.right = temp
        
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.postorder(root)
        return root

        
        
        
