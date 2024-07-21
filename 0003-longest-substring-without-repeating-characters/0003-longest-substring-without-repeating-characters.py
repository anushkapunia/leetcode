class Solution(object):
    def lengthOfLongestSubstring(self, s):
    
        char_index = {}
        max_length = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in char_index:
                start = max(start, char_index[char] + 1)
            max_length = max(max_length, i - start + 1)
            char_index[char] = i
        
        return max_length
        