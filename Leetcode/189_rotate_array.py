class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[0 : n - k] = nums[0 : n - k][::-1]
        print(nums)
        nums[n - k :] = nums[n - k:][::-1]
        print(nums)
        nums[:] = nums[::-1]
