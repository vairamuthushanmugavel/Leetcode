class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr,x)
        results = collections.deque()
        left = idx -1
        right = idx
        while len(results) < k and left >= 0 and right < len(arr):
            a = arr[left]
            b = arr[right]
            if abs(a - x) <= abs(b-x):
                results.appendleft(a)
                left = left -1
            else:
                results.append(b)
                right = right + 1
            
        while len(results) < k and left >=0:
            results.appendleft(arr[left])
            left = left -1
        while len(results) < k and right < len(arr):
            results.append(arr[right])
            right = right +1
        
        return results
                