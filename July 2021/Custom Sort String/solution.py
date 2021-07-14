from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordermap = defaultdict(lambda:30)
        for idx in range(len(order)):
            ordermap[order[idx]] = idx
            
        return "".join(sorted(list(s),key = lambda x:ordermap[x]))