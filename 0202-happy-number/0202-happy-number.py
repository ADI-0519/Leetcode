class Solution:
    def isHappy(self, n: int) -> bool:
        
        hashset = set()

        while not(n in hashset):
            if n == 1:
                return True
            else:
                hashset.add(n)    
                n = self.new_no(n)

        return False



    def new_no(self,n):
        summation = 0
        while n > 0:
            last_digit = n % 10
            n //= 10
            summation += last_digit ** 2

        return summation