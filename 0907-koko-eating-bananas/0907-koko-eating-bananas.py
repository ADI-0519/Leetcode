import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def condition(speed):
            # can we finish everything given this number
            cnt = 0
            
            for pile in piles:
                cnt += math.ceil(pile / speed)
                

            return True if cnt <= h else False
        
        l,r = 1,max(piles)

        while l < r:
            mid = l + (r-l) // 2

            if condition(mid):
                r = mid
            else:
                l = mid + 1

        return l