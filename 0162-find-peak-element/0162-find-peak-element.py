class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        l,r = 0,len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2

            if mid < 1:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    l = mid + 1


            if mid >= len(nums)-1:
                if nums[mid-1] < nums[mid]:
                    return mid

                else:
                    r = mid - 1

            else:
                
                # check neighbours

                if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                    return mid

                elif nums[mid-1] > nums[mid+1]:
                    r = mid - 1

                else:
                    l = mid + 1
