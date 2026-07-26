class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = r = heights.index(max(heights))
        m = min([heights[l],heights[r]]) * (r-l)

        for i in range(r+1,len(heights)):
            v = min(heights[l],heights[i])* (i-l)
            if v >= m:
                m = v
                r = i

        for i in reversed(range(0,l)):
            v = min(heights[i],heights[r])* (r-i)   
            if v >= m:
                m = v
                l = i
        return m            

        