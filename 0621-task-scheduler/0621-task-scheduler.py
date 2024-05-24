class Solution:
    def leastInterval(self, tasks, n): 
        f = [0]*26
        for t in tasks:
            f[ord(t)- ord('A')]+=1
            
        pq = [-fr for fr in f if fr>0]
        
        heapq.heapify(pq)
        time = 0
        while pq:
            cycle = n+1
            task = 0
            s=[]
            while cycle> 0 and pq:
                cf = - (heapq.heappop(pq))
                if cf >1:
                    s.append(-(cf-1))
                    
                task+=1
                cycle-=1
            for f in s:
                heapq.heappush(pq,f)
        
                
            time+= task if not pq else n+1
            
        return time    
            


            
            
            
            
            