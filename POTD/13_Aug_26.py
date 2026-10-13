class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        nums = [num * num for num in nums]
        nums.sort()
        print(nums)
        l , r = 0, len(nums) - 1
        res = 0
        while l < r :
            res += -nums[l] + nums[r]
            l += 1
            r -= 1
        if r - l + 1 % 2 != 0 :
            res += nums[r]
        return res




        