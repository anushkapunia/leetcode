class Solution(object):
    def rotate(self, nums, k):
        
        t = []
        n = len(nums)
        k = k%n
        for i in range(n):
            t.append(nums[i])
            
        for i in range(k,n):
            nums[i] = t[i-k]
            
        for i in range(k):
            nums[i] = t[n-k+i]
            
        
            

        
        

        

                

        