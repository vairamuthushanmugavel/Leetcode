class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        subarray_length = 0
        sum = 0
        countMap = {}
        for i in range(len(nums)):
            sum += - 1 if nums[i] == 0 else 1
            if sum == 0:
                if subarray_length < i + 1:
                    subarray_length = i + 1
            elif sum in countMap:
                if subarray_length < i - countMap[sum]:
                    subarray_length = i - countMap[sum]
            else:
                countMap[sum] = i
        return subarray_length