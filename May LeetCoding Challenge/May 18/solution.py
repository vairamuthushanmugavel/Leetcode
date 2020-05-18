from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            s1count = Counter(s1)
            s2count = Counter()
            s1len = len(s1)
            s2len = len(s2)
            isPermutation = False
            for i in range(s2len):
                s2count[s2[i]] += 1
                if i >= s1len:
                    if(s2count[s2[i - s1len]] == 1):
                        del s2count[s2[i - s1len]]
                    if(s2count[s2[i - s1len]] > 1):
                        s2count[s2[i - s1len]] -=1
                if s1count ==  s2count:
                    isPermutation = True
                    break
            return isPermutation