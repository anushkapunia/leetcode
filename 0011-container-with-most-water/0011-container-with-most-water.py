class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        maxa = 0
        
        while l<r:
            minht = min(height[l],height[r])
            area = minht*(r-l)
            maxa = max(area, maxa)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

            
       
            
        return maxa     
    
            
            
            
            
            
        
        