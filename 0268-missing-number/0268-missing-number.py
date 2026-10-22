class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        summ = sum(nums)
        return sum(range(1,n+1)) - summ