class Solution:
    def maxArea(self, height):
        l,r = 0,len(height)-1
        m = -1
        while(l<r):
            a,b = height[l],height[r]
            if a<b:
                area = a*(r-l)
                while(height[l]<=a):
                    l+=1
            else:
                area = b*(r-l)
                while(height[r]<=b) and r:
                    r-=1
            m = max(m,area)
        return m