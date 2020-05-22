class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        # print(row,col)
        dp = [[ 0  for i in range(col)] for j in range(row)]
        # print(dp)
        # print(col)
        count = 0
        #populating the dp table for the first row
        for i in range(col):
            dp[0][i] = matrix[0][i]
            count +=  dp[0][i]
        
        #populating the dp table for the first column
        for i in range(1,row):
            dp[i][0] = matrix[i][0]
            count += dp[i][0]
        
        # print(dp)
        #populating the dp table and calculating the count 
        
        for i  in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == 1:
                    dp[i][j] = 1+min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
                count += dp[i][j]
        
        return count
        
        