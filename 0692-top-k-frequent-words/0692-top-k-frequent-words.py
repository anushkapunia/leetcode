class Solution(object):
    def topKFrequent(self, words, k):
 
        cnt=defaultdict(lambda :[0,""])
        for i in words:
            cnt[i]=[cnt[i][0]-1,i]
        lst=list(cnt.values())
        heapq.heapify(lst)
        lst=heapq.nsmallest(k,lst)
        ans=[]
        for i in lst:
            ans.append(i[1])
        return ans
        