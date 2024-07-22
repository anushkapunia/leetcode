class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        maxl = 0
        chars = {}
        for i , char in enumerate(s):
            if char in chars:
                start = max(start, chars[char]+1)
            chars[char] = i
            maxl = max(maxl, i-start+1)
            
        return maxl
            
        