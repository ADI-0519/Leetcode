class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return len(nums)
        
        i = 1
        freq = 1

        for j in range(1,len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                freq = 1
                i += 1
                
            elif freq <= 1:
                nums[i] = nums[j]
                freq += 1
                i += 1

        return i