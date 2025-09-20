class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ""
        for element in address:
            if element == ".":
                s += "[.]"
            else:
                s += element

        return s