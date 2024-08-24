class Solution(object):
    def isValid(self, s):
        b = { '(' : ')' , '{' : '}' , '[' : ']'}
        h = ['(' , '[' , '{']
        stack = []
        for a in s:
            if a in h:
                stack.append(a)
            elif stack and a == b[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return stack == []
        
    