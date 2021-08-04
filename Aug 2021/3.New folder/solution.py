from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = []
        res = [[]]
        
        def uniqId(lst):
            return Counter(lst)
        
        def calcPowerSet(currset,idx):
            _uniqId  = uniqId(currset)
            if _uniqId in seen:
                return
            seen.append(_uniqId)
            res.append(currset)

            
            for nIdx in range(idx+1,len(nums)):                    
                calcPowerSet(currset+[nums[nIdx]],nIdx )
            
            
        
        
        for idx in range(len(nums)):
            currset = [nums[idx]]
            calcPowerSet(currset,idx)

        return res
        