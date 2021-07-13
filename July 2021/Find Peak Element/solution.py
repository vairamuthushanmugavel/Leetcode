class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0,float("-inf"))
        nums.append(float("-inf"))
        
        for idx in range(1,len(nums)-1):
            if nums[idx] > nums[idx-1] and nums[idx] > nums[idx+1]:
                return idx -1
        return 0