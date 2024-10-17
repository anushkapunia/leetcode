class Solution(object):
    def reverse(self, x):
        s = str(x)
        
        if x<0:
            a = '-' + (s[ :0:-1])
        else:
            a = s[ : :-1]
        i = int(a)
        if -2**31 < i < 2**31-1:
            return i
        else:
            return 0
   