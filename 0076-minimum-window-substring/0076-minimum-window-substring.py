class Solution(object):
    def minWindow(self, s, t):
        if t in s:
            return t
        
        l = defaultdict(int)
        
        for char in t:
                l[char]+=1
                
        left = 0
        rr , rl = 0 ,0
        cd =defaultdict(int)
        c = 0
        minl = float('inf')
        cl = 0
    
        for r in range(len(s)):
            w = s[r]
            
            if w in t:
                cd[w]+=1
                if cd[w] == l[w]:
                     c+=1
                
                
            
                
            while c == len(l):
                cl = r - left +1
                
                if cl < minl:
                        minl = cl
                        rr , rl = r, left
                        
                if s[left] in cd:
                    cd[s[left]]-=1
                    if cd[s[left]] < l[s[left]]:
                        
                         c-=1
                    
                left+=1
                
        return s[rl:rr+1] if minl!=float('inf') else ""
                
                    
               
                
                

        
        