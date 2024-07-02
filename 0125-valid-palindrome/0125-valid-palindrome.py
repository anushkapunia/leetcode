class Solution(object):
    def isPalindrome(self, s):
        a = "".join(char.lower() for char in s if char.isalnum())
        
        return a == a[: :-1]

            
        
        