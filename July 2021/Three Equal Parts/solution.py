class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        impossible = [-1,-1]
        numOf1s = arr.count(1)
        if numOf1s == 0:
            return [0,2]
        if numOf1s % 3 != 0:
            return impossible
        
        numOf1sPerPart = numOf1s / 3
        
        idxOf1inpart0 = -1
        idxOf1inpart1 = -1
        idxOf1inpart2 = -1
        
        temp = 0
        
        for idx in range(len(arr)):
            if arr[idx]:
                temp += arr[idx]
                
                if numOf1sPerPart + 1 == temp:
                    idxOf1inpart1 = idx
                elif 2* numOf1sPerPart +1 == temp:
                    idxOf1inpart2 = idx
                elif temp == 1:
                    idxOf1inpart0 = idx
                    
        print(idxOf1inpart0,idxOf1inpart1,idxOf1inpart2)
        while idxOf1inpart2 < len(arr):
            if (arr[idxOf1inpart0] == arr[idxOf1inpart1]) and (arr[idxOf1inpart1] == arr[idxOf1inpart2]):
                    
                    idxOf1inpart0 += 1
                    idxOf1inpart1 += 1
                    idxOf1inpart2 += 1
            else:
                print("from here")
                return impossible
        
        
        return [idxOf1inpart0 - 1, idxOf1inpart1]

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    