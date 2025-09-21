class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        pref = [0] * n
        suff = [0] * n
        maxx = height[0]
        maxx2 = height[n-1]

        for i in range(1,len(height)):
            
            pref[i] = maxx
            suff[n-i-1] = maxx2

            maxx = max(maxx,height[i])
            maxx2 = max(maxx2,height[n-1-i])

        water = 0
        
        for i in range(1,len(height)-1):
            h1, h2 = pref[i],suff[i]

            water += max((min(h1,h2) - height[i]),0) 

        return water