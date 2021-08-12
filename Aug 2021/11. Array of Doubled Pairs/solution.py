class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        count = collections.Counter(arr)
        for key in count:
            if count[key] == 0:
                continue
            if key < 0 and key % 2 != 0:
                return False
            target = key / 2 if key < 0 else key * 2
            
            if count[key] > count[target]:
                return False
            
            count[target] = count[target] - count[key]
        
        return True
            
            
            
            
        