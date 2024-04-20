class Solution(object):
    def minAddToMakeValid(self, s):
        l,r = 0,0
    
        for w in s:
            if w =="(" :
                l+=1
            else:
                l-=1
            if l ==-1:
                r+=1
                l=0
                
        return l+r       
                
        
            
                
                     
        
        