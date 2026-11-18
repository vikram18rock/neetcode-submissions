class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

        tillPivot = 0
        for i in range(len(nums)):
            if (tillPivot == sum - tillPivot - nums[i]):
                return i
            tillPivot += nums[i]

        return -1