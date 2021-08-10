class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        i = 0
        zerosCount = 0
        onesCount = 0
        while i < len(s):
            if s[i] == '0':
                i += 1
            else:
                break
        
        for idx in range(len(s)):
            if s[idx] == '0':
                zerosCount += 1
            else:
                onesCount += 1
            if zerosCount > onesCount:
                zerosCount = onesCount
        return zerosCount             