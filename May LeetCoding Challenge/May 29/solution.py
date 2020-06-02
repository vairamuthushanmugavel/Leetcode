class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # forming the adjecency List
        adjList = [[] for i in range(numCourses)]
        for src, target in prerequisites:
            adjList[src].append(target)
        # container for maintaning visited nodes.
        visited = [0 for i in range(numCourses)]

        def isCyclic(index):
            if visited[index] == 2:
                return True
            visited[index] = 2  # started processing
            curr_adj = adjList[index]
            for ele in curr_adj:
                if isCyclic(ele):
                    return True

            visited[index] = 1  # ended processing
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if isCyclic(i):
                    return False
        return True
        