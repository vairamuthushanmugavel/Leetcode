from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_length, p_length = len(s), len(p)
        result = []
        sMap = [0] * 26
        pMap = [0] * 26
        # generating the frequency map
        for i in p:
            pMap[ord(i) - ord('a')] += 1

        # Looping over the source string
        for i in range(s_length):
            sMap[ord(s[i]) - ord('a')] += 1
            if i >= p_length-1:
                isAnagram = True
                for r in range(len(pMap)):
                    if(sMap[r] != pMap[r]):
                        isAnagram = False
                        break
                if isAnagram:
                    result.append(i - p_length + 1)

                sMap[ord(s[i - p_length + 1]) - ord('a')] -= 1
        
        return result