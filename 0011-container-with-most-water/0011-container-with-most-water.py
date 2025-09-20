class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        p1,p2 = 0,len(height)-1
        maxx = 0
        while p1 < p2:
            width = (p2-p1)
            h = min(height[p1],height[p2])
            area = width * h
            maxx = max(maxx,area)

            if height[p1] < height[p2]:
                p1 += 1

            else:
                p2 -= 1

        return maxx