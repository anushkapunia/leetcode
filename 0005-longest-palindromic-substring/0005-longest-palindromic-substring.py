class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
        
        for i in range(len(s)):
            # Check for odd-length palindromes
            palindrome1 = expandAroundCenter(i, i)
            # Check for even-length palindromes
            palindrome2 = expandAroundCenter(i, i + 1)
            
            # Update longest palindrome found
            longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)

        return longest_palindrome
        