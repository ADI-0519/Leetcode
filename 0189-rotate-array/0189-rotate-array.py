class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        steps = k % len(nums)
        n = len(nums)
        nums[:] = nums[(n-steps):] + nums[:(n-steps)]
        