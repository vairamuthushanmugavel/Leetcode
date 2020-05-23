class Solution:
    def intervalIntersection(self, A, B):
        apointer = 0
        bpointer = 0
        intervals = []
        while apointer <  len(A) and bpointer < len(B):
            start,end = max(A[apointer][0],B[bpointer][0]),min(A[apointer][1],B[bpointer][1])
            if start <=  end:
                intervals.append([start,end])
            if A[apointer][1] < B[bpointer][1]:
                apointer += 1
            else:
                bpointer += 1
        return intervals