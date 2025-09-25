class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        n = len(potions)
        arr = []
        for element in spells:
            l,r = 0,n-1
            while l < r:
                mid = l + (r-l) //2

                if element * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1

            if l == n-1 and element * potions[l] < success:
                arr.append(0)

            else:
                arr.append(len(potions)-l)

        return arr