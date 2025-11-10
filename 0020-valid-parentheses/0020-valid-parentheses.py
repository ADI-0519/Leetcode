class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {")":"(","}":"{","]":"["}
        stk = []

        for element in s:
            if element in hashmap.keys():

                if stk and stk[-1] == hashmap[element]:
                    stk.pop()

                else:
                    return False

            else:
                stk.append(element)

        return True if len(stk) == 0 else False