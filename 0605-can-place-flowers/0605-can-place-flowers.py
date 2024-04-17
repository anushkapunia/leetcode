class Solution(object):
    def canPlaceFlowers(self, fb, n):
        count = 0
        for i in range(len(fb)):
            if fb[i] == 0:
                left = (i == 0) or (fb[i - 1] == 0)
                right = (i == len(fb) - 1) or (fb[i + 1] == 0)
                if left and right:
                    fb[i] = 1
                    count+=1
                if count>=n:
                    return True
                
        return count>=n