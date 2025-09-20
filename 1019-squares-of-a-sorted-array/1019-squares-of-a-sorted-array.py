class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        new_arr = []

        while l<=r:
            if abs(nums[l])>abs(nums[r]):  
                new_arr.append(nums[l]**2)
                l += 1

            else:
                new_arr.append(nums[r]**2)
                r -= 1

        new_arr.reverse()
        return new_arr
        