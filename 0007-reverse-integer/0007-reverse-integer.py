class Solution(object):
    def reverse(self, x):
    
        s = str(x)

        if x < 0:
            # Handle negative numbers: reverse the part after the minus sign
            reversed_str = '-' + s[:0:-1]
        else:
            # Reverse the positive number as a string
            reversed_str = s[::-1]

        # Convert the reversed string back to an integer
        reversed_int = int(reversed_str)

        # Check if the reversed number is within the 32-bit signed integer range
        if -2**31 <= reversed_int <= 2**31 - 1:
            return reversed_int
        else:
            return 0  # Return 0 if the reversed integer overflows

        