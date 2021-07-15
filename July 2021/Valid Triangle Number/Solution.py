class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for right in range(len(nums)-1,-1,-1):
            left ,mid = 0, right -1
            while left < mid:
                if nums[left] + nums[mid] > nums[right]:
                    count = count + (mid - left)
                    mid = mid -1
                else:
                    left = left + 1
        return count
            
        