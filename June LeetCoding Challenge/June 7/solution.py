class Solution:
    def findsol(self,coins, i, amount,dp):
        if amount == 0: return 1
        if amount < 0 or i == len(coins): return 0
        if dp[i][amount] != -1 : return dp[i][amount]

        dp[i][amount] = self.findsol(coins, i, amount - coins[i],dp) + self.findsol(coins, i+1, amount,dp)
        return dp[i][amount]
    
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for j in range(amount+1)] for i in range(len(coins))]
        return self.findsol(coins, 0,amount,dp)
