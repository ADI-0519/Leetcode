class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        
        while l<=r:
            mid = (l+r) // 2
            arr = matrix[mid]
            l2,r2 = 0,len(arr)-1

            while l2 <= r2:
                midpoint = (l2+r2) // 2
                if arr[midpoint] == target:
                    return True
                elif arr[midpoint] > target:
                    r2 = midpoint - 1
                else:
                    l2 = midpoint + 1

            print(l2,r2)

            if r2 == -1:
                r = mid - 1
            else:
                l = mid + 1

            


        return False
