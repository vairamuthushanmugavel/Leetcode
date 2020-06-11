class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length-1,0,-1):
            for i in range(i):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1],nums[i] 
        