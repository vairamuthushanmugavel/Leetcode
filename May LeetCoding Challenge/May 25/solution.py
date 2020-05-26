class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        alen, blen = len(A), len(B)
        dp = [[0 for i in range(blen+1)] for j in range(alen+1)]
        # populating the dp table
        for i in range(alen):
            for j in range(blen):
                if(A[i] == B[j]):
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j + 1])
        return dp[alen][blen]