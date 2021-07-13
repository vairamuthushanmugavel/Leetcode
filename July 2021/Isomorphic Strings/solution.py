from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}
        rmapping = {}
        
        for x , y in zip(s,t):
            if x in mapping and mapping[x] != y:
                return False
            mapping[x] = y
            if y in rmapping and rmapping[y] != x:
                return False
            rmapping[y] = x
            
        return True