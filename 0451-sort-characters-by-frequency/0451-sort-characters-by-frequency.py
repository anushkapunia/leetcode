class Solution(object):
    def frequencySort(self, s):
        t = Counter(s)
        a = sorted(t.items() , key = lambda x:-x[1])
        return ''.join(c*f for c,f in a)