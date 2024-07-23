class Solution(object):
    def minWindow(self, s, t):
  
        if not s or not t:
            return ""

        if t in s:
            return t

        letter_dict = {}
        for letter in t:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1

        required = len(letter_dict)
        formed = 0
        window_counts = {}
        left = 0
        min_len = float('inf')
        result = ""

        for right, char in enumerate(s):
            if char in letter_dict:
                window_counts[char] = window_counts.get(char, 0) + 1
                if window_counts[char] == letter_dict[char]:
                    formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]

                left_char = s[left]
                if left_char in letter_dict:
                    window_counts[left_char] -= 1
                    if window_counts[left_char] < letter_dict[left_char]:
                        formed -= 1
                left += 1

        return result
        