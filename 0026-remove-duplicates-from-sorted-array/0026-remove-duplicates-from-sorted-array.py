class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Handle edge case for empty array

    # Initialize the pointer for the position of the next unique element
        unique_pos = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_pos]:  # Found a new unique element
                unique_pos += 1  # Move the unique pointer
                nums[unique_pos] = nums[i]  # Update the value at the unique pointer
    
        return unique_pos + 1  # The 
        
        