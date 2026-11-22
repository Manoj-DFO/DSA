class Solution:
    def longestNonRepeatingSubstring(self, s):

        left = maximum = 0
        last_seen = [-1]*128

        for i in range(len(s)):

            char = ord(s[i])
            left = max(left, last_seen[char] + 1)
            last_seen[char] = i
            maximum = max(maximum, i - left + 1)

        return maximum