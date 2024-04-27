class Solution(object):
    def maximumScore(self, a, b, c):
        
        maximum = max(a, b, c)
        minimum = min(a, b, c)
        middle = a + b + c - maximum - minimum

        if minimum + middle < maximum:
            return minimum + middle

        return (a + b + c) // 2
        