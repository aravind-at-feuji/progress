class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [1] * len(nums)
        pro = 1
        for i in range(len(nums)) :
            pro *= nums[i]
            left[i] = pro
        pro = 1
        for i in range(len(nums) - 1,-1,-1) :
            pro *= nums[i]
            right[i] = pro
        for i in range(len(nums)) :
            if i - 1 >= 0 :
                res[i] *= left[i - 1]
            if i + 1 < len(nums) :
                res[i] *= right[i + 1]
        return res