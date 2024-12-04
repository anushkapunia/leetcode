class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0  # Already at the last index
    
        jumps = 0
        current_end = 0
        farthest = 0
    
        for i in range(n - 1):  # No need to consider the last index
        # Update the farthest index reachable
            farthest = max(farthest, i + nums[i])
        
        # If we reach the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
            
            # Early stop if we've reached or passed the last index
                if current_end >= n - 1:
                    break
    
        return jumps
        