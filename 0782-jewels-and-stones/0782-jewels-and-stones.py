class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashset = set()
        total = 0
        for element in jewels:
            if element not in hashset:
                hashset.add(element)

        for element in stones:
            if element in hashset:
                total += 1

        return total