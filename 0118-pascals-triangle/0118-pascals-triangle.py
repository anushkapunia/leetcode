class Solution(object):
    def generate(self, numRows):
        
        f = []
        for i in range(1,numRows+1):
            t = [1]
            r = 1
            for c in range(1,i):
                
                r*=i - c
                r//=c
                t.append(r)
            f.append(t)
                
    
        return f
                
        