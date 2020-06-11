from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q =  deque()
        for char in s:
            q.append(char)
        for char in t:
            if q[0] == char:
                q.popleft()
        return len(q)==0
        

