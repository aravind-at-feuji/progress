class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        end = nums[len(nums) - 1]
        if end < k :
            return k
        res = -1
        for i in range(k,end + 1,k) :
            res = i
            if i not in nums :
                return i
        return res + k
        