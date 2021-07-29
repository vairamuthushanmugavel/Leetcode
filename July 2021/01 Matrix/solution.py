from collections import deque
class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        de = deque()
        
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    de.append((row,col))
                else:
                    mat[row][col] = -1
        
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        level = 0
        while len(de) > 0:
            level += 1
            size = len(de)
            for _ in range(size):
                curr = de.popleft()
                for direc in directions:
                    row = curr[0]+ direc[0]
                    col = curr[1] + direc[1]

                    if row < 0 or col < 0 or row == rows or col == cols or mat[row][col] != -1:
                        continue
                    mat[row][col] = level
                    de.append((row,col))

        return mat
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    