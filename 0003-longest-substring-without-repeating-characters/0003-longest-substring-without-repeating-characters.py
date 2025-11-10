class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        p1 = 0
        hashset = set()
        maxx = 0

        for p2 in range(len(s)):
            # remove

            while s[p2] in hashset:
                hashset.remove(s[p1])
                p1 += 1

            # add
            hashset.add(s[p2])

            # check

            maxx = max(len(hashset),maxx)

        return maxx