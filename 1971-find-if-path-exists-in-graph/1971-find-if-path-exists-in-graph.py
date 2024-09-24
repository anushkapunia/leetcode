class Solution(object):
    def validPath(self, n, edges, source, destination):
        from collections import defaultdict
        
        d = defaultdict(list)
        for u , v in edges:
            d[u].append(v)
            d[v].append(u)
        
        v = set()
        def dfs(source , destination):
            
            if source == destination:
                return True
            v.add(source)
            for a in d[source]:
                if a not in v:
                    if dfs(a,destination):
                        return True
            return False
        return dfs(source,destination)
                
            
        
        
        