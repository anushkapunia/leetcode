class Solution(object):
    def getRow(self, rowIndex):
        r = [1]
        a = 1
        for i in range(rowIndex):
            a*=rowIndex-i
            a//=i+1
            r.append(a)
            
        return r
            
              
            
        