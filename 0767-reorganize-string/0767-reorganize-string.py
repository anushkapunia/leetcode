
class Solution(object):
    def reorganizeString(self, s):
        c = Counter(s)
        
        h= [(-count, char) for char,count in c.items()]
        
        heapq.heapify(h)
        n = len(s)
        if -h[0][0] > (n+1)//2:
            return ""
        
        result = []
        while len(h)>= 2:
            count1,char1= heapq.heappop(h)
            count2,char2 = heapq.heappop(h)
            
            result.extend([char1,char2])
            
            if -count1>1:
                heapq.heappush(h,(count1+1 , char1))
                
            if - count2 > 1:
                heapq.heappush (h, (count2+1 , char2))
                
        if h:
            result.append(h[0][1])
            
        return ''.join(result)

                
                
                
        

