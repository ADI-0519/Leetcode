class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        hashset = set()
        longest = 0
        n = len(s)

        for p2 in range(len(s)):
            while s[p2] in hashset:
                hashset.remove(s[p1])
                p1 += 1

            hashset.add(s[p2])
            if ((p2-p1) + 1) > longest:
                longest = (p2-p1) + 1

        return longest