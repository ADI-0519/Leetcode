class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max,r_max = height[0],height[n-1]
        l,r = 0,n-1
        water = 0
        while l < r:
            if l_max <= r_max:
                water += l_max - height[l]
                l += 1

            else:
                water += r_max - height[r]
                r -= 1

            l_max = max(l_max,height[l])
            r_max = max(r_max,height[r])


        return water