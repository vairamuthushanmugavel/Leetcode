class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        added =  set()
        if length == 0: return []
        result = []
        nums.sort()
        for i in range(length-2):
            j = i +1 
            k = length - 1
            while j < k :
                total = nums[j] + nums[k] + nums[i]
                if total  == 0:
                    if (nums[i],nums[j],nums[k]) not in added:
                        result.append([nums[i],nums[j],nums[k]])
                        added.add((nums[i],nums[j],nums[k]))
                    k -=1 
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return result