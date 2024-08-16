
class Solution(object):
    def findMedianSortedArrays(self, n1, n2):
        i , j = 0 , 0
        m = len(n1)
        n = len(n2)
        a = []
        
        while i < m and j < n:
            if n1[i] < n2[j]:
                a.append(n1[i])
                i+=1
            else:
                a.append(n2[j])
                j+=1
                
        while i < m:
            a.append(n1[i])
            i+=1
            
        while j < n:
            a.append(n2[j])
            j+=1
            
        l = len(a)
        if l % 2 == 1:
            i = l//2
            return a[i]
        else:
            i = l//2
            return (a[i] + a[i-1])/2.0
                
                
        
        