class Solution(object):
    def frequencySort(self, s):
        c = Counter(s)
        
        return ''.join(char * freq for char , freq in c.most_common())
        
        