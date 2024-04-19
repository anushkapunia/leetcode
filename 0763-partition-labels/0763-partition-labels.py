class Solution(object):
    def partitionLabels(self, S):
        l = []
        d={c:i for i ,c in enumerate(S)}
        s,e=0,0
        for i,c in enumerate(S):
            e = max(e,d[c])
            if i == e:
                l.append(i-s+1)
                s = i+1
               
        return l   
        
            
            
        