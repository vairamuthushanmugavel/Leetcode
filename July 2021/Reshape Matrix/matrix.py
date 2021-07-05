class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        matrow = len(mat)
        matcol = len(mat[0])
        
        if (matrow*matcol != r * c):
            return mat
        
        
        
        arr = []
        for row in mat:
            for col in row:
                arr.append(col)
        
        output = []
        for row in range(r):
            colstart = row * c
            currarr = arr[colstart:colstart+c]
            output.append(currarr)
        
        return output
            