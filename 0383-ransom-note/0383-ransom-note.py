class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap_A = {}
        hashmap_B = {}
        for element in magazine:
            hashmap_A[element] = hashmap_A.get(element,0) + 1

        for element in ransomNote:
            hashmap_B[element] = hashmap_B.get(element,0) + 1

        for key in hashmap_B:
            if hashmap_B[key] > hashmap_A.get(key,0):
                return False
            
        return True