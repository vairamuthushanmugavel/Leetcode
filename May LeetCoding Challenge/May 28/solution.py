class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        result.append(0)
        for i in range(1, num+1):
            result.append(result[i & i - 1] + 1)
        return result