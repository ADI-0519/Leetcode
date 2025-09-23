class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        left, right = 0, x
        while left <= right:
            middle = (right + left) // 2
            
            if middle * middle == x:
                return middle
            elif middle * middle < x:
                left = middle + 1
            else:
                right = middle - 1
        return right 
