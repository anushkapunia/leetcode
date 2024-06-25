class Solution(object):
    def maxResult(self, nums, k):

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque([0])  # store indices
        
        for i in range(1, n):
            # remove indices outside the window
            if dq[0] < i - k:
                dq.popleft()
            
            dp[i] = nums[i] + dp[dq[0]]
            
            # remove indices with smaller values
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            
            dq.append(i)
        
        return dp[n-1]