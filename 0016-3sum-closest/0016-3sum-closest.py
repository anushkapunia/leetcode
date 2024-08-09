class Solution(object):
    def threeSumClosest(self, nums, target):
    
        nums.sort()
        n = len(nums)
        closest_sum = sum(nums[:3])
    
        if closest_sum >= target:
            return closest_sum

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            left, right = i + 1, n - 1
        
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
            
                if current_sum == target:
                    return current_sum
            
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
            
                if current_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            
            # Early termination
                if closest_sum == target:
                    return closest_sum
    
        return closest_sum
        