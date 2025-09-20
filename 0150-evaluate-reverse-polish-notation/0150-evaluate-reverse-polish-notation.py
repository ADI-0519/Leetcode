
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        hashset = {"+","-","*","/"}

        for element in tokens:
            if element in hashset:
                a,b = stk.pop(),stk.pop()
                if element == "+":
                    stk.append(a+b)

                elif element == "-":
                    stk.append(b-a)

                elif element == "*":
                    stk.append(a*b)

                elif element == "/":
                    stk.append(trunc(b/a))

                
            
            else:
                stk.append(int(element))


        return stk[-1]