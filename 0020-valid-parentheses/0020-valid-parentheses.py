class Solution(object):
    def isValid(self, s):
       
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Stack to keep track of opening brackets
        stack = []
        
        # Iterate over the string
        for char in s:
            if char in bracket_map:
                # Pop the topmost element from the stack if it's not empty
                # Otherwise, use a dummy value (e.g., '#') to avoid index errors
                top_element = stack.pop() if stack else '#'
                
                # Check if the top element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly matched
        return not stack
