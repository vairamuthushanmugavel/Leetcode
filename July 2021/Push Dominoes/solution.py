from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
       
        rightarr = [-1 for _ in range(N)]
        
        leftarr = [-1 for _ in range(N)]
        
        tempidx = -1
        
        for idx in range(N):
            if dominoes[idx] == "R":
                tempidx = idx
            elif dominoes[idx] == "L":
                tempidx = -1
            rightarr[idx] = tempidx
                
                
                
            
        tempidx = -1
        
        for idx in range(N-1,-1,-1):
            if dominoes[idx] == "L":
                tempidx = idx
            
            elif dominoes[idx] == "R":
                tempidx = -1
            
            leftarr[idx] = tempidx

        ans =[None for _ in range(N)]
        
        for idx in range(N):
            if dominoes[idx] == ".":
                leftidx = leftarr[idx]
                rightidx = rightarr[idx]

                leftdiff = float("inf") if leftidx == -1 else abs(idx - leftarr[idx])
                rightdiff = float("inf") if rightidx == -1 else abs(idx - rightarr[idx])

                if leftdiff == rightdiff:
                    ans[idx] = "."
                elif leftdiff < rightdiff:
                    ans[idx] = "L"
                elif rightdiff < leftdiff:
                    ans[idx] = "R"
            
            else:
                ans[idx] = dominoes[idx]
        return "".join(ans)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            