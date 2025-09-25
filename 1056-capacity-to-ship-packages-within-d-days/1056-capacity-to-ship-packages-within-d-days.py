import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # boundary from not feasible to feasible

        def condition(limit):
            cnt = 0
            days_taken = 1
            i = 0
            while i < len(weights):
                if (cnt+weights[i]) <= limit:
                    cnt += weights[i]
                    i += 1

                else:
                    days_taken += 1
                    cnt = 0
                    
            return True if days_taken <= days else False  


        l,r = max(weights), sum(weights)

        while l < r:
            mid = l + (r-l) // 2

            if condition(mid):
                r = mid

            else:
                l = mid + 1

        return l