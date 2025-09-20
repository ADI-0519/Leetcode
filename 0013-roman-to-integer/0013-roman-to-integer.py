class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total = 0
        for i in range(len(s)-1):
            if s[i] == "I" and s[i+1] == "V":
                total -= 1
                continue
            elif s[i] == "I" and s[i+1] == "X":
                total -= 1
                continue
            elif s[i] == "X" and s[i+1] == "L":
                total -= 10
                continue
            elif s[i] == "X" and s[i+1] == "C":
                total -= 10
                continue
            elif s[i] == "C" and s[i+1] == "D":
                total -= 100
                continue
            elif s[i] == "C" and s[i+1] == "M":
                total -= 100
                continue

            total += hashmap[s[i]]
            print(total)

        total += hashmap[s[-1]]

        return total