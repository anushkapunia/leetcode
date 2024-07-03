class Solution(object):
    def threeSum(self, nums):
  
        nums.sort()  # Sort the array
        n = len(nums)
        result = set()  # Use a set to avoid duplicates

        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return [list(x) for x in result]
        