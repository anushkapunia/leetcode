class Solution(object):
    def minimumSwap(self, s1, s2):
        xy_count = 0  # Count of 'x' to 'y' swaps needed
        yx_count = 0  # Count of 'y' to 'x' swaps needed
        
        for m, n in zip(s1, s2):
            if m != n:
                if m == 'x':
                    xy_count += 1
                else:
                    yx_count += 1
        
        # Check if the total count of swaps is even
        total_swaps = xy_count + yx_count
        if total_swaps % 2 != 0:
            return -1
        
        # Calculate the minimum number of swaps needed
        min_swaps = xy_count // 2 + yx_count // 2
        
        # Check if there's an odd count of 'x' to 'y' swaps
        if xy_count % 2 == 1:
            min_swaps += 2  # Add 2 additional swaps to resolve unresolvable situations
        
        return min_swaps


