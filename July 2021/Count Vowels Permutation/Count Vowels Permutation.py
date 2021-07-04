
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        chars = ['a','e','i','o','u']
        count = 0
        mod = 1000000007
        dp = dict()

        def findCount(currchar,rmCount):
            if rmCount == 0:
                return 1
            if (currchar,rmCount) in dp:
                return dp[(currchar,rmCount)]
            
            total = 0

            if currchar == "a":
                total =  findCount("e",rmCount-1) % mod
            elif currchar ==  "e":
                total =  (findCount("a",rmCount-1) + findCount("i",rmCount -1)) % mod
            elif currchar == "i":
                total =  (findCount("a",rmCount-1) + findCount("o",rmCount -1) + findCount("e",rmCount-1) + findCount("u",rmCount-1)) % mod
            elif currchar == "o":
                total = (findCount("i",rmCount-1) + findCount("u",rmCount -1)) % mod
            elif currchar == "u":
                total = (findCount("a",rmCount-1) ) % mod

            dp[(currchar,rmCount)] = total
            return total 




        for char in  chars:
            count = (count + findCount(char,n-1)) % mod  

        return count

