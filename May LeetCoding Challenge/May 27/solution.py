class Solution:
    def bfs(self, colored, node, matrix):
        colored[node] = 1
        queue = []
        queue.append(node)
        while len(queue) > 0:
            curr = queue.pop()
            for ele in matrix[curr]:
                if colored[ele] == colored[curr]:
                    return False
                if colored[ele] == -1:
                    colored[ele] = 1 - colored[curr]
                    queue.append(ele)
        return True
    
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
                # forming the adjecency matrix
        adjecency = [[] for i in range(N+1)]
        for dislike in dislikes:
            adjecency[dislike[0]].append(dislike[1])
            adjecency[dislike[1]].append(dislike[0])
        colored = [-1 for i in range(N+1)]
        for i in range(1, N+1):
            if colored[i] == -1:
                if self.bfs(colored, i, adjecency) is not True:
                    return False

        return True
        