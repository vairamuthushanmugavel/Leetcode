class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # print("")
        N =len(piles)
        alex = 0
        lee = 0
        start = 0
        end = len(piles) - 1
        for idx in range(N):

            if (idx + 1) % 2 != 0:
                #alex turn
                temp = 0
                if piles[start] > piles[end]:
                    temp = piles[start]
                    start += 1
                else: 
                    temp = piles[end]
                    end -= 1
                # print("alex",temp)
                alex += temp

            else:

                temp = 0
                if piles[start] < piles[end]:
                    temp = piles[start]
                    start += 1
                else: 
                    temp = piles[end]
                    end -= 1
                # print("lee",temp)
                lee += temp        
        
        
        
        return alex > lee