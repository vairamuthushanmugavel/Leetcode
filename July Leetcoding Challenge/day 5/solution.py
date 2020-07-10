class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        count = 0
        while result > 0:
            count = count + (result & 1)
            result =  result >> 1
        return count
