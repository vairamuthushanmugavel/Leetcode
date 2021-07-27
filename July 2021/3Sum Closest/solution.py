class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = math.inf
        
        for i in range(0,len(nums)-2):
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                currsum = nums[i]+nums[start]+nums[end]
                if currsum > target:
                    end -= 1
                else:
                    start += 1
                
                if abs(currsum-target) < abs(closestSum - target):
                    closestSum =  currsum
        return closestSum
            