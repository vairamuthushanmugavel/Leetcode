class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        gridId = 2
        gridval = dict()
        gridval[0] = 0        

        def getSizeandAssignId(r,c):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or grid[r][c] != 1:
                return 0
            
            grid[r][c] = gridId
            
            return 1 + getSizeandAssignId(r+1,c) + getSizeandAssignId(r-1,c) + getSizeandAssignId(r,c+1) +                                 getSizeandAssignId(r,c-1)
                        
        
        
        # Assign ids and sizes.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = getSizeandAssignId(r,c)
                    gridval[gridId] = size
                    gridId += 1
                    
        
        print(gridval)
        #calculating the max value
        res = gridval[2] if 2 in gridval else 0
        

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    temp = set()
                    temp.add( grid[r-1][c] if r > 0 else 0 )
                    temp.add(grid[r+1][c] if r < rows-1 else 0)
                    temp.add(grid[r][c-1] if c > 0 else 0)
                    temp.add(grid[r][c+1] if c < cols-1 else 0)

                    total = 1
                    for _id in temp:
                        total = total + gridval[_id]
                    res = max(res,total)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                