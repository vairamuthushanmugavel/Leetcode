# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
            root = TreeNode(preorder[0])
            for val in preorder[1:]:
                current =  root
                while True:
                    if val < current.val:
                        if current.left is None:
                            current.left = TreeNode(val)
                            break
                        current = current.left
                            
                    if val > current.val:
                        if current.right is None:
                            current.right = TreeNode(val)
                            break
                        current = current.right
                         
            return root