class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap_s, hashmap_t = {},{}
        for element in s:
            hashmap_s[element] = hashmap_s.get(element,0) + 1
        for element in t:
            hashmap_t[element] = hashmap_t.get(element,0) + 1

        for letter in hashmap_s:
            if hashmap_s[letter] != hashmap_t.get(letter,0):
                return False

        return True

        