# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = deque()
        count = 0
        queue.append([root,1])
        while len(queue) != 0:
            length = len(queue)
            first = queue[0]
            last = queue[-1]
            while length:
                currNode = queue.popleft()
                curr = currNode[0]
                idx = currNode[1]
                if curr.left != None :
                    queue.append([curr.left,2*idx])
                if curr.right != None : 
                    queue.append([curr.right,2*idx+1 ])
                length -= 1
            count = max(count , ( (last[1] - first[1]) + 1 ))
        return count