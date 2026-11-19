class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find all differences from target
        s = {}
        for i in range(len(nums)):
            s[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in s and s[target - nums[i]] != i:
                return [i, s[target - nums[i]]]
        return []
        # return if any match