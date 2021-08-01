class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        ans =  [[0 for _ in range(cols)] for _ in range(rows)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(i,j):
            if i < 0 or i > rows-1 or j < 0 or j > cols-1:
                return float("inf")
            
            if visited[i][j]:
                return float("inf")

            if mat[i][j] == 0:
                return 0

            visited[i][j] = True
            
            val = 1 + min(dfs(i-1,j),dfs(i+1,j),dfs(i,j-1),dfs(i,j+1))

            visited[i][j] = False

            return val
        
        
        
        for i in range(rows):
            for j in range(cols):
                #checking cell is one.if it is 0,nothing needs to be done
                if mat[i][j] == 1:
                    ans[i][j] = dfs(i,j)
        return ans


sol  = Solution()
ins = [[1,1,1],[1,1,1],[1,1,1]]
print(sol.updateMatrix(ins))                    
