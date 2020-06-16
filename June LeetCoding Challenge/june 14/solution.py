class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        self.fare = float('inf')
        # defining the adjcency matrix
        add_mat = [[] for i in range(n)]
        for node in flights:
            add_mat[node[0]].append((node[1], node[2]))

        # print(add_mat)
        def dfs(currsrc, currfare, k):
            if k < -1:
                return
            if currfare > self.fare:
                return 
            if currsrc == dst:
                self.fare = min(self.fare, currfare)
                return
            edges = add_mat[currsrc]
            for edge in edges:
                if len(edge) > 0:

                    dfs(edge[0], currfare+edge[1], k-1)
        dfs(src, 0, K)
        if self.fare == float('inf'):
            return -1
        else:
            return self.fare