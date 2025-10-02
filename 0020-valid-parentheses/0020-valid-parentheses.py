class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {")":"(","}":"{","]":"["}
        stk = []

        for element in s:
            if element in brackets:
                if not stk or stk[-1] != brackets.get(element,None):
                    return False

                stk.pop()

            else:
                stk.append(element)
            
        return True if len(stk) == 0 else False