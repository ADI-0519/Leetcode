class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less,equal,greater = [],[],[]

        for element in nums:
            if element < pivot:
                less.append(element)

            elif element > pivot:
                greater.append(element)

            else:
                equal.append(element)

        nums = less + equal + greater
        return nums