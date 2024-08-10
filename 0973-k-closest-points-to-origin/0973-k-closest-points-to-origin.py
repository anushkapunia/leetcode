class Solution(object):
    def kClosest(self, points, k):
        if not points or k<=0:
            return []
        
        mh = []
        for i , (x,y) in enumerate(points):
            d = x**2 + y**2
            if len(mh) <k:
                heappush(mh , (-d,i))
            else:
                heappushpop(mh, (-d,i))
                
        return [points[i] for _ , i in mh]

                
            
        
        