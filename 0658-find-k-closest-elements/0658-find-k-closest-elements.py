class Solution(object):
    def findClosestElements(self, arr, k, x):
    
        left = 0
        right = len(arr) - 1
    
        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
    
        return arr[left:right+1]