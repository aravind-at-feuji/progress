# Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ditn = dict()
        for i in range(len(nums)) :
            if target - nums[i] in ditn :
                return [i,ditn[target - nums[i]]]
            ditn[nums[i]] = i
        return []