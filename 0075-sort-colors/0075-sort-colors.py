class Solution(object):
    def sortColors(self, arr):
        l , m , h = 0,0,len(arr)-1
        while m <= h:
            if arr[m] == 0:
                arr[m] , arr[l] = arr[l] , arr[m]
                m+=1
                l+=1
            elif arr[m] == 1:
                m+=1
            else:
                arr[h] , arr[m] = arr[m] , arr[h]
                h-=1
            
        