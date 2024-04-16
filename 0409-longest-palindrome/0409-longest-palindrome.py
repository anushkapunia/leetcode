class Solution(object):
    def longestPalindrome(self, s):
        count = {}
        for letter in s:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
        result = 0
        for freq in count.values():
            if freq%2 ==0:
                result +=freq
                
        odd = False
        for freq in count.values():
            if freq%2==1:
                result +=freq-1
                odd = True
            
        if odd == True:
            result +=1
            
        return result    
            
