class Solution(object):
    def reverse(self,x):
        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)
        while x:
            mod = x % 10
            rev = (rev*10) + mod
            x //= 10
            if rev > 2**31 - 1:
                return 0
        return sign * rev

        return int(inverse)
            

        