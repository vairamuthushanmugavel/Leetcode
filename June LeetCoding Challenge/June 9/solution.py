from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        q =  deque()
        for char in s:
            q.append(char)
        for char in t:
            if len(q) == 0:
                break
            if q[0] == char:
                q.popleft()
        return len(q)==0