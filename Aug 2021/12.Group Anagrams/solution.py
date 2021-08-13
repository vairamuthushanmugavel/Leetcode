from collections import defaultdict,Counter

def getKey(string):
    return "".join(sorted(string))

class Solution:

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for word in strs:
            
            key = getKey(word)
            
            dd[key].append(word)
        return dd.values()
        