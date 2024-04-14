
    # Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    def minOperations(self,arr):
        operations=0
        for i in range(len(arr)-1):
            if arr[i+1]<=arr[i]:
                diff = arr[i]-arr[i+1] +1
                arr[i+1]=arr[i+1]+diff
                operations=operations +diff
        return operations 
        
       