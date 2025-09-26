class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = max(nums),sum(nums)
        
        def condition(split):
            cnt = 0
            required_k = 1

            for element in nums:
                cnt += element

                if cnt > split:
                    required_k += 1
                    cnt = element

                    if required_k > k:
                        return False

            return True

        while l < r:
            mid = l + (r-l) // 2

            if condition(mid):
                r = mid

            else:
                l = mid + 1

        return l