# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        queue = [ ]
        ans = [ ]
        queue.append([root])
        while len(queue):
            tempque = []
            tempval = []
            curr = queue.pop(0)
            for i in curr:
                tempval.append(i.val)
                if i.left is not None:
                    tempque.append(i.left)
                if i.right is not None:
                    tempque.append(i.right)
            if len(tempque):        
                queue.append(tempque)
            ans.insert(0,tempval) 
        return ans
