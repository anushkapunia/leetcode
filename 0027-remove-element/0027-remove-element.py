class Solution(object):
    def removeElement(self, nums, val):
        
        k = 0  # Pointer for the position of non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val element to the k-th position
                k += 1
        return k
        
        