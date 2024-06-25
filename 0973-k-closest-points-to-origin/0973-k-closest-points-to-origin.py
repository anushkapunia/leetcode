class Solution(object):
    def kClosest(self, points, k):
 
        maxHeap = []
        for id, p in enumerate(points):
            d = p[0] * p[0] + p[1] * p[1]
            if len(maxHeap) < k:
                heappush(maxHeap, (-d, id))
            else:
                heappushpop(maxHeap, (-d, id))

        return [points[id] for _, id in maxHeap]  