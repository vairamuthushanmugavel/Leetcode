from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ctr = Counter(arr)
        vals = list(ctr.values())
        vals.sort(reverse=True)
        
        count = 0
        i = 0
        N = len(arr)
        totaln = N
        
        while totaln > N/2:
            totaln = totaln - vals[i]
            count = count + 1
            i = i + 1
        return count 