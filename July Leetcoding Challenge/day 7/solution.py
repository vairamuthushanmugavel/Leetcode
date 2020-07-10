class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         if rows == 0: return 0
#         cols = len(grid[0])
#         perimeter = 0
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] != 0:
#                     if row-1 < 0 or grid[row -1 ][col] == 0:
#                         perimeter += 1
#                     if  row+1 >= rows or grid[row+1][col] == 0:
#                         perimeter += 1
                    
#                     if col -1 < 0  or grid[row][col-1] == 0:
#                         perimeter +=1 
#                     if col + 1 >= cols or grid[row][col+1] == 0:
#                         perimeter += 1
#         return perimeter
        rows =  len(grid)
        if rows == 0: return 0
        cols =  len(grid[0])
        
        def perimeter(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols :
                return 1
            if grid[i][j] == 2:
                return 0
            if grid[i][j] == 0:
                return 1
            #marking that node has been processed already
            grid[i][j] =  2
            
            return perimeter(i+1,j) + perimeter(i-1,j) + perimeter(i,j+1) + perimeter(i,j-1)
            
           
        
        
        for row in range(rows):
            for col in range(cols):
               if grid[row][col] != 0 and grid[row][col] != 2 :
                    return perimeter(row,col)