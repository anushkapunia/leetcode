class Solution(object):
    def findSubstring(self, s, words):
        index = []
        w = Counter(words)
        start = 0
        l = len(words[0])
        
        
        for i in range(l):
            start = i
            window = defaultdict(int)
            wc = 0
            
            for j in range(i , len(s) - l+1 , l):
                word = s[ j : j + l]
                
                if word not in words:
                    start = j+l
                    window = defaultdict(int)
                    wc = 0
                    continue
                
                window[word]+=1
                wc+=1
                
                while window[word] > w[word]:
                    window[s[start : start + l]] -=1
                    start = start+ l
                    wc-=1
                    
                if wc == len(words):
                    index.append(start)
                    
        return index 
                    
        