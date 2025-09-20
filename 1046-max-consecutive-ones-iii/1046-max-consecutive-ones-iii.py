class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        p1 = 0
        longest = 0
        zeroes = 0

        for p2 in range(len(nums)):

            if nums[p2] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[p1] == 0:
                    zeroes -= 1

                p1 += 1

            length = (p2-p1) + 1
            if length > longest:
                longest = length


        return longest
                