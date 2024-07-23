class Solution(object):
    def minWindow(self, s, t):
      
        if not s or not t:
            return ""

        # Optimize the initial check
        if len(t) == 1:
            return t if t in s else ""

        target_counts = Counter(t)
        window_counts = Counter()
        required = len(target_counts)
        formed = 0
        left = 0
        min_len = float('inf')
        result = ""

        for right, char in enumerate(s):
            window_counts[char] += 1
            
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]

                window_counts[s[left]] -= 1
                if s[left] in target_counts and window_counts[s[left]] < target_counts[s[left]]:
                    formed -= 1
                left += 1

        return result
        