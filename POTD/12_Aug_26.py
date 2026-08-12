class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l , r = 0,0
        maxFreq = 0
        ditn = {}
        res = 0
        while r < n :
            ditn[nums[r]] = ditn.get(nums[r] , 0 ) + 1
            maxFreq = max(ditn.get(nums[r]),maxFreq)

            while l <= r and maxFreq > k :
                freq = ditn.get(nums[l],0)
                ditn[nums[l]] = ditn.get(nums[l],0) - 1
                if freq >= maxFreq :
                    maxFreq = freq - 1
                l += 1
            r += 1
            res = max(res, r - l + 1)
        
        return res - 1