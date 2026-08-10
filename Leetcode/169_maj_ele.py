class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        maj = nums[0]
        for i in range(len(nums)) :
            if maj == nums[i] :
                cnt += 1
            else :
                cnt -= 1
            if cnt < 0 :
                maj = nums[i]
                cnt = 1
        return maj                
        