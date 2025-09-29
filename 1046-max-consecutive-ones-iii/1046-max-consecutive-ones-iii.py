class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        wrong = 0
        p1 = 0
        maxx = 0
        for p2 in range(len(nums)):

            if nums[p2] == 0:
                wrong += 1

            while wrong > k:
                if nums[p1] == 0:
                    wrong -= 1

                p1 += 1

            maxx = max(maxx,(p2-p1)+1)

        return maxx