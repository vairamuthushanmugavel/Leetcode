"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root is None:
            return res
        deq = deque()
        deq.append(root)
        
        while len(deq) > 0:
            temp = []
            N = len(deq)
            for _ in range(N):
                curr = deq.popleft()
                temp.append(curr.val)
                
                for child in curr.children:
                    deq.append(child)
            res.append(temp)
        return res

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        