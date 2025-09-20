class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        small=min(strs)
        large=max(strs)

        for i,s in enumerate(small):
            if small[i]!=large[i]:
                return small[:i]
        
        return small
