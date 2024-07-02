class Solution(object):
    def twoSum(self, numbers, t):
        seen = {}
        for i , num in enumerate(numbers):
            a = t - num
            if a in seen:
                return [seen[a]+1 , i+1]
            
            seen[num] = i
            
        return []
      
        
                
        
        
        
        
        
        
        
        