# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root = None
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        def createTree(left,right):
            if left > right:
                return None
            mid = (left + right)//2
            node = TreeNode(nums[mid])
            node.left = createTree(left, mid-1)
            node.right = createTree(mid+1,right)
            return node
        
        return createTree(0,len(nums)-1)
        
             