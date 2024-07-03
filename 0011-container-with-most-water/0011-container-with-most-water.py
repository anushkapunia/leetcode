class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) -1
        maxa = 0
        a = 0
        while l < r:
            d = r - l
            minh = min(height[l] , height[r])
            a = d * minh
            maxa = max(a , maxa)
            
            if height[l] > height[r]:
                r = r-1
                
            else:
                l = l+1
                
        return maxa

        