class Solution(object):
    def minSetSize(self, arr):
        d = {}
        for i in arr:
            d[i]= d.get(i,0)+1
            
        s = sorted(d.values(),reverse= True)
        total = len(arr)
        remove = 0
        minset= 0
        for v in s:
            remove+=v
            minset+=1
            if remove>=total//2:
                break
        return minset        
            
            