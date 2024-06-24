class Solution(object):
    def leastInterval(self, tasks, n):
      
        task_counts = [0] * 26
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        
        # Find the maximum frequency
        max_freq = max(task_counts)
        
        # Count how many tasks have the maximum frequency
        max_count = task_counts.count(max_freq)
        
        # Calculate the minimum number of intervals required
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
        