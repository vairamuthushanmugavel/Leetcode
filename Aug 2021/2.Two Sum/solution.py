class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in hashmap:
                return [idx,hashmap[complement]]
            hashmap[nums[idx]] = idx