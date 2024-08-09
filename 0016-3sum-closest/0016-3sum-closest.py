class Solution(object):
    def threeSumClosest(self, nums, target):
  
        nums.sort()  # Sort the array
        closest_sum = float('inf')  # Initialize with infinity

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If the current sum is closer to the target than the closest sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1  # Move the left pointer to the right
                elif current_sum > target:
                    right -= 1  # Move the right pointer to the left
                else:
                    return current_sum  # If the current sum is exactly equal to the target

        return closest_sum  # Return the closest sum found
