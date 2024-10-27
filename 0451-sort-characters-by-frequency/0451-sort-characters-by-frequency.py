class Solution(object):
    def frequencySort(self, s):
        t = Counter(s)
        return ''.join(c*f for c,f in t.most_common())
        