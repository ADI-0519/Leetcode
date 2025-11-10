class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        arr = [0] * n

        for i,element in enumerate(temperatures):
            while stk and element > temperatures[stk[-1]]:
                index = stk.pop()
                arr[index] = i - index
            
            stk.append(i)

        return arr

                       