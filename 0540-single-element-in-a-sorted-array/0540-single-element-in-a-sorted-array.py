class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1

        while l <= r:
            mid = l + (r-l) // 2
            

            if mid < 1 or mid >= n-1:
                return nums[mid]

            else:
                # check neighbours:

                behind = nums[mid-1]
                after = nums[mid+1]

                if behind == nums[mid]:
                    if (mid-1) % 2 == 0:
                        l = mid + 1
                    else:
                        r = mid - 1

                elif after == nums[mid]:
                    if (mid+1) % 2 == 1:
                        l = mid + 1

                    else:
                        r = mid - 1

                else:
                    return nums[mid]