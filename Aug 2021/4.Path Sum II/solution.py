# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        def calculateSum( currNode, currarr,currsum):
            if currNode is None:
                return 
            if  currsum + currNode.val == targetSum and (currNode.left is None and currNode.right is None):
                res.append(currarr + [currNode.val])
                
            if currNode.left is not None:
                calculateSum(currNode.left, currarr + [currNode.val],currsum + currNode.val)
            
            if currNode.right is not None:
                calculateSum(currNode.right, currarr + [currNode.val],currsum + currNode.val)
        
        calculateSum(root,[],0)
        return res
            