class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # duplicate solutions prevention
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            p1,p2 = i+1,len(nums)-1

            while p1 < p2:
                summ = nums[p1] + nums[p2] + nums[i]

                if summ == 0:
                    arr.append([nums[i],nums[p1],nums[p2]])
                    p1,p2 = p1 + 1, p2 - 1

                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1

                    while p1 < p2 and nums[p2] == nums[p2+1]:
                        p2 -= 1

                elif summ < 0:
                    p1 += 1

                else:
                    p2 -= 1

        return arr
