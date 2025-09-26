import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # boundary from not feasible to feasible

        def condition(limit):
            cnt = 0
            days_taken = 1
            
            for element in weights:

                cnt += element
                if cnt > limit:
                    cnt = element
                    days_taken += 1

                    if days_taken > days:
                        return False
                    
            return True


        l,r = max(weights), sum(weights)

        while l < r:
            mid = l + (r-l) // 2

            if condition(mid):
                r = mid

            else:
                l = mid + 1

        return l