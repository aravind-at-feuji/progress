class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        rob1 , rob2 = 0 , 0
        for i in range(n) :
            temp = max(nums[i] + rob1 , rob2)
            rob1 = rob2
            rob2 = temp
        return rob2