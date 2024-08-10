class Solution(object):
    def kClosest(self, points, k):
        mh = []
        for i , p in enumerate(points):
            d = p[0]*p[0] + p[1]*p[1]
            if len(mh) <k:
                heappush(mh , (-d,i))
            else:
                heappushpop(mh, (-d,i))
                
        return [points[i] for _ , i in mh]

                
            
        
        