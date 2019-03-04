class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,len(height)-1
        min = 0
        while(i<j):
            if(height[i]<=height[j]):
                temp = height[i]
                if(temp*(j-i)>min):
                    min = temp*(j-i)
                i+=1
            if(height[i]>height[j]):
                temp = height[j]
                if(temp*(j-i)>min):
                    min = temp*(j-i)
                j-=1
        return min