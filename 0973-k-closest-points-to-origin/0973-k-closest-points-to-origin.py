class Solution(object):
    def kClosest(self, points, k):
        if not points or k<=0:
            return []
        
        mh = []
        for i , p in enumerate(points):
            d = p[0]*p[0] + p[1]*p[1]
            if len(mh) <k:
                heappush(mh , (-d,i))
            else:
                heappushpop(mh, (-d,i))
                
        return [points[i] for _ , i in mh]

                
            
        
        