class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)<len(word2):
            length = len(word1)
        else:
            length = len(word2)

        string = ""    
        for i in range(length):
            string += word1[i]
            string += word2[i]

        string += word1[length:]
        string += word2[length:]

        return string