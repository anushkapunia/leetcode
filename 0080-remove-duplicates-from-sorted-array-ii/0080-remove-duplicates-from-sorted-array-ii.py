class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:  # If the array has 2 or fewer elements, it's already valid
            return n

        insert_pos = 2  # Start inserting from the 3rd position

        for i in range(2, n):
        # Compare the current element with the element two places behind
            if nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos  
        