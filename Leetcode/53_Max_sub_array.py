class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        l , r = 0, 0
        s = 0
        res = max(nums)
        while r < len(nums) :
            s += nums[r]
            while s < 0 :
                l = r
                s = 0
            r += 1
            res = max(res,s)
        if res == 0 and res not in nums :
            return max(nums)
        return res
