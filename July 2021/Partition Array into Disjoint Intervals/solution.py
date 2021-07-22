class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        right = [0 for _ in range(len(nums))]
        mn = float("inf")
        for idx in range(len(nums)-1,-1,-1):
            mn = min(mn,nums[idx])
            right[idx] = mn
        
        mx = float("-inf")
        for idx in range(len(nums)-1):
            mx = max(mx,nums[idx])
            if mx <= right[idx+1]:
                return idx + 1
        